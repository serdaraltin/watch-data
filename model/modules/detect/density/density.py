import cv2
import numpy as np
import time
import logging
import queue
import threading

from config.config_manager import config,preset
from database.connector.connector_postgre import DensityDatabase
from services.logging.logger import custom_logger
from model import Density

class DensityTable():
    #def __init__(self) :
    def __init__(self, camera_id=12) -> None:

        self.camera_id = str(camera_id)
        logging.info(f"Initializing Table for camera_id: {self.camera_id}")

        
        self.config_source = config.setting.processing.source[self.camera_id]

        self.video_path = self.config_source["video_path"]
        self.table_coordinates = np.array(self.config_source["point_data"]["points_masa"])
        self.json_table_coordinates = self.config_source["point_data"]["points_masa"]

        # self.video_path="rtsp://minoa:Minoa2024.@45.139.203.25:554/Streaming/Channels/1301"
        # self.table_coordinates=  [ 
        # [(923, 386), (1093, 296), (1249, 368), (1052, 496), (971, 452)],
        # [(700, 268), (844, 193), (982, 274), (830, 396), (741, 351)],
        # [(780, 196), (626, 265), (576, 270), (545, 215), (695, 167)],
        # [(461, 161), (548, 133), (586, 100), (614, 135), (486, 196)],
        # [(203, 282), (360, 208), (307, 274), (283, 326), (237, 344)],
        # [(65, 318), (133, 290), (163, 382), (69, 390), (66, 361)],
        # [(53, 481), (129, 459), (242, 511), (167, 636), (64, 675)],
        # [(80, 776), (113, 957), (398, 954), (305, 768), (186, 733)],
        # [(307, 326), (347, 279), (406, 252), (455, 308), (371, 415)],
        # [(654, 447), (534, 324), (453, 357), (432, 476), (502, 555)],
        # [(545, 624), (634, 743), (794, 745), (742, 507), (607, 565)]
        # ]
        self.check_interval = 5
        self.last_check_time = time.time()

        self.summary_interval = 60
        self.last_summary_time = time.time()

        self.frame_skip = 2
        
        self.motion_detected_recently = {i: False for i in range(len(self.table_coordinates))}
        self.motion_count = {i: 0 for i in range(len(self.table_coordinates))}
        self.last_analysis = {i: 0 for i in range(len(self.table_coordinates))}
        self.table_statutes = ["bos"] * len(self.table_coordinates)
        self.cap = cv2.VideoCapture(self.video_path)
        
        self.DensityDataDB= DensityDatabase()
        self.db_write_queue = queue.Queue()
        self.flush_interval = 10  
        self.timer = threading.Timer(self.flush_interval, self.flush_database)
        self.timer.start()

    def write_database(self, data):
        try:
            self.DensityDataDB.set_data(data)
            self.DensityDataDB.commit()
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

    def calculate_area(self, points):
        contour = np.array(points, dtype=np.int32)
        area = cv2.contourArea(contour)
        return area

    def determine_pixel_threshold(self, area, video_area):
        if 800000 < video_area < 1000000:
            if 10000 < area:
                return 200
            elif 5000 <= area <= 10000:
                return 100
            elif area < 5000:
                return 50
        elif 1000000 < video_area:
            if 20000 < area:
                return 300
            elif 10000 <= area <= 20000:
                return 300
            elif area < 10000:
                return 300

    def draw_tables_and_numbers(self,frame, table_coordinates, motion_detected_recently):
        """Her bir masa için çerçeve çizer, masa numarasını ve doluluk durumunu yazar."""
        for index, points in enumerate(table_coordinates):
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))

            cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
            

            x_min = min(pts[:,0,0])
            y_min = min(pts[:,0,1])
            
            status = "dolu" if motion_detected_recently[index] else "bos"
            
            cv2.putText(frame, f"Masa {index+1}: {status}", (x_min, y_min - 5), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    def extract_region(self, frame, points):
        """Verilen noktalara göre bir çerçeveden bölge çıkarır."""
        mask = np.zeros_like(frame)
        cv2.fillPoly(mask, [np.array(points)], (255, 255, 255))
        return cv2.bitwise_and(frame, mask)

    def process_frame(self, frame1, frame2, points, table_index,pixel_thresholds):
        """Belirli bir bölgede iki çerçeve arasındaki hareketi tespit eder."""
        region1 = self.extract_region(frame1, points)
        region2 = self.extract_region(frame2, points)
        diff = cv2.absdiff(region1, region2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    
        motion_detected = False

        for contour in contours:
            if cv2.contourArea(contour) > pixel_thresholds[table_index]: 
                self.motion_count[table_index] += 1
            break

    def check_tables_status(self):

        self.current_time = time.time()

        if self.current_time - self.last_check_time >= self.check_interval:
            for index in range(len(self.table_coordinates)):

                if self.motion_count[index] > 0:
                    self.motion_detected_recently[index] = True
                    status = "dolu"
                    self.last_analysis[index]+=1
                else:
                    self.motion_detected_recently[index] = False
                    status = "bos"
                    
                print(f"Masa {index + 1}: {status}")
                self.motion_count[index] = 0  
            self.last_check_time = self.current_time
            print("************************")

    def update_panel_info(self, frame):
        """Sol üst köşede yarı saydam bir panel üzerine masaların durumunu yazar."""
        panel_height = 20 + 20 * len(self.table_statutes)  # Panel yüksekliğini hesapla
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (250, panel_height), (0, 0, 0), -1)  # Panel boyutu
        cv2.addWeighted(overlay, 0.3, frame, 0.7, 0, frame)  # Yarı saydam arka plan

        for index, status in enumerate(self.table_statutes):
            if status == "bos":
                cv2.putText(frame, f"Masa {index + 1}: {status}", (10, 20 + index * 20), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            elif status == "dolu":
                cv2.putText(frame, f"Masa {index + 1}: {status}", (10, 20 + index * 20), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    def summarize_tables_status(self):

        print("Dakika Sonu Analizi :")
        for index, count in self.last_analysis.items():
            status = 1 if count > 6 else 0
            print(f"Masa Hareket Sayısı   : {index + 1}: {count}")
            print(f"Masa Durumu{index + 1}: {status}")
            self.table_statutes[index]=status
            self.last_analysis[index]=0
        # Sözlüğü sıfırla
        for index in self.motion_count:
            self.motion_count[index] = 0
        self.last_summary_time = time.time()
        return self.table_statutes

    def run(self):
        try:
            #cap = cv2.VideoCapture(self.video_path)
            print("1")
            ret, frame1 = self.cap.read()
            height, width = frame1.shape[:2]
            print(f"HEIGHT : {height},  WIDTH : {width}")
            video_area = width * height
            table_areas = [self.calculate_area(points) for points in self.table_coordinates]
            pixel_thresholds = [self.determine_pixel_threshold(area, video_area) for area in table_areas]
            frame_count = 0

            while True:

                ret, frame2 = self.cap.read()
                frame_count += 1

                if not ret:
                    print("Görüntü alinamadi.")
                    break
                if frame_count % self.frame_skip == 0:
                    for index, points in enumerate(self.table_coordinates):
                        self.process_frame(frame1, frame2, points, index,pixel_thresholds)
                    self.check_tables_status()
                    frame1 = frame2.copy()

                    self.draw_tables_and_numbers(frame2, self.table_coordinates, self.motion_detected_recently)
                    
                    current_time = time.time()
                    if self.current_time - self.last_summary_time >= self.summary_interval:
                        print("status time")
                        db_table_statutes = self.summarize_tables_status()

                        for i in range(len(self.table_coordinates)):
                            
                            density_example = Density(
                                camera_id = self.config_source["camera_id"],
                                label = "density",
                                additional = self.json_table_coordinates[i],
                                status= db_table_statutes[i]
                            )
                            
                            data = density_example.to_dict()
                            print("data :",data)
                            self.queue_database_write(data)

                            custom_logger.info(f"Dining Table Status concluded. Data:\n{data}\n\n", exc_info=True)
                        
                    self.update_panel_info(frame2)
                    #cv2.imshow('Masalar', frame2)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        except Exception as ex:
            print(f"An error occurred: {ex}")




