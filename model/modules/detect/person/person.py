
import cv2
import os
import numpy as np
from ultralytics import YOLO
import random
import logging
from datetime import timezone
import datetime
from collections import defaultdict, OrderedDict
import torch
from config.config_manager import config, preset

# from services.logger import custom_logger
from lib.gui.drawing import draw_rectangle, draw_text, draw_highlighted_rectangle, draw_polylines, draw_line, draw_person_informations
from lib.mathematic.functions import is_crossing_line
from lib.gui.window_video import show_window
from model import Person, EnterExit, Gender, Age
import queue
import threading

from model.model_statistic import Statistic
if (config.setting.module.detect["gender"]):
    from modules.detect.gender.gender import PredGender
from database.connector.connector_postgre import PersonDatabase
from utils.check_camera_connection import schedule_cam_check

from services.logging.logger import custom_logger



class PersonCounter():
    
    def __init__(self, camera_id) -> None:

        self.camera_id = str(camera_id)
        logging.info(f"Initializing PersonCounter for camera_id: {self.camera_id}")

        
        self.config_source = config.setting.processing.source[self.camera_id]

        self.line_start = np.array(self.config_source["point_data"]["points"][0])
        self.line_end = np.array(self.config_source["point_data"]["points"][1])
        self.video_path = self.config_source["video_path"]
        self.enter_direction = self.config_source["point_data"]["enter_direction"]
        # user_data = ""

        model_name, model_type = config.setting.model.detect["person"].values()
        model_path = os.path.join('modules/detect/person/model', f"{model_name}.{model_type}")

        # self.model = YOLO(model_path).to(config.setting.device)
        self.model = YOLO(model_path)
        self.threshold_time = datetime.timedelta(seconds=15)

        self.track_history = defaultdict(lambda: [])
        self.last_crossing_time = defaultdict(lambda: None)

        self.statistics = Statistic()

        self.enter_exit_counter = {
            "enter": 0,
            "exit": 0
        }

        self.PersonDataDB = PersonDatabase()


       
        self.db_write_queue = queue.Queue()
        self.flush_interval = 10  
        self.timer = threading.Timer(self.flush_interval, self.flush_database)
        self.timer.start()

        if(config.setting.module.detect["gender"]):
            self.gender_pred = PredGender()

    def write_database(self, data):
        try:
            self.PersonDataDB.set_data(data)
            self.PersonDataDB.commit()
            custom_logger.info("Data successfully written to the database.")
        except Exception as e:
            custom_logger.error("Error writing data to the database: ", exc_info=True)

    def flush_database(self):
        try:
            while not self.db_write_queue.empty():
                data = self.db_write_queue.get()
                self.write_database(data)
                self.db_write_queue.task_done()
        except Exception as e:
            custom_logger.error("Error flushing the database: ", exc_info=True)
        finally:
            self.timer = threading.Timer(self.flush_interval, self.flush_database)
            self.timer.start()



    def queue_database_write(self, data):
        self.db_write_queue.put(data)
    
    
 
    def process_frame(self, frame):
        results = self.model.track(frame, persist=True, verbose=False)
        annotated_frame = frame.copy()

        if results[0].boxes is not None and results[0].boxes.id is not None and results[0].boxes.cls is not None:
            person_boxes = [box for box, cls in zip(results[0].boxes.xywh.cpu(), results[0].boxes.cls.int().cpu().tolist()) if cls == 0]
            person_track_ids = [track_id for track_id, cls in zip(results[0].boxes.id.int().cpu().tolist(), results[0].boxes.cls.int().cpu().tolist()) if cls == 0]

            for box, track_id in zip(person_boxes, person_track_ids):
                x_center, y_center, w, h = box
                x_left = int(x_center - w / 2)
                y_top = int(y_center - h / 2)
                feet_point = np.array([x_center, y_top + h - 30])  # Point at the feet of the person

                draw_rectangle(annotated_frame, x_left, y_top, w, h)
                draw_text(annotated_frame, f"ID: {track_id}", x_left, y_top - 10)


                track = self.track_history[track_id]
                track.append(feet_point)  # Append feet point

                if len(track) > 1:
                    crossing_result = is_crossing_line(track[-2], track[-1], self.line_end, self.line_start, self.enter_direction)
                    if crossing_result is not False:
                        current_time = datetime.datetime.now()+datetime.timedelta(hours=3)
                        print(current_time)
                  
                        if self.last_crossing_time[track_id] is None or (current_time - self.last_crossing_time[track_id]) > self.threshold_time:
                                                                        
                            gender = random.choice(["male", "female"])
                            if(config.setting.module.detect["gender"]):
                                gender = self.gender_pred.predictions(annotated_frame, x_left, y_top, x_left + int(w), y_top + int(h))

                            if crossing_result:  # Entering
                                method = "enter"
                                self.enter_exit_counter["enter"] += 1

                            else:  # Exiting
                                method = "exit"
                                self.enter_exit_counter["exit"] += 1
                            
                            # print(gender_)
                            model_enter_exit = EnterExit(
                                person_id = 1,
                                event_time = current_time.isoformat(),
                                event_type = method
                            )

                            print("="*60)
                            print(gender)
                            print("="*60)
                        
                        
                            model_gender = Gender(
                                person_id = 1,
                                gender = gender,
                                confidence = 0.5
                            )

                            age_range = random.choice(["0-18", "19-30", "31-45", "46-60", "61+"])

                            model_age = Age(
                                person_id=1,
                                age_range=age_range,
                                confidence=0.95)


                            person_example = Person(
                                age=model_age,
                                gender=model_gender,
                                enter_exit=model_enter_exit,
                                camera_id=self.config_source["camera_id"],
                                detection_time=current_time.isoformat(),
                                label="person",
                                confidence=0.85)
                            
                            # print(person_example)
                            data = person_example.to_dict()
                          
                            # self.queue_database_write(data)
                            custom_logger.info(f"Person detect. Data:\n{data}\n\n", exc_info=True)


                            self.statistics.push(person_example)
                            self.last_crossing_time[track_id] = current_time


                            draw_highlighted_rectangle(annotated_frame, x_left, y_top, w, h)
                            
                        # Eski verileri temizleme
                        for id_ in list(self.track_history.keys()):
                            if current_time - self.last_crossing_time.get(id_, current_time) > datetime.timedelta(minutes=1):
                                del self.track_history[id_]
                                del self.last_crossing_time[id_]
                                
                if len(track) > 30:   
                    track.pop(0)


                
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                draw_polylines(annotated_frame, [points], color=(0, 0, 255), thickness=2)
            draw_line(annotated_frame, self.line_start, self.line_end)
                
        draw_person_informations(annotated_frame, self.statistics.enter, self.statistics.exit, self.statistics.male, self.statistics.female, self.statistics.current_female, self.statistics.current_male)

        show_window(annotated_frame) # Görüntü pencerede açılması

    def start(self):
        try:
            cap = cv2.VideoCapture(self.video_path)
        
            skip_count = 0

        

            while cap.isOpened():
                success, frame = cap.read()

                if not success:
                    print("="*80,"Warning: Camera streaming not available.","="*80)

                    schedule_cam_check(self.video_path)
                    
                if success and skip_count % config.setting.processing.threshold_time_default == 0:
                    self.process_frame(frame)
                
                    
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break

                skip_count += 1


            custom_logger.info("Video processing completed.")
        except Exception as e:
            custom_logger.error("Error starting video capture: ", exc_info=True)

        finally:
            cap.release()
            cv2.destroyAllWindows()
            custom_logger.info("Video capture and windows successfully released and destroyed.")
        