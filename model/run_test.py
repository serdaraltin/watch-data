# from tests import run_test
# import datetime
# import random
# # from multiprocessing import Process
from config import config
from modules.detect.density.density import DensityTable
# import os, torch

# from model.model_statistic import Statistic
# from model.model_person import Person, EnterExit, Gender, Age
# from modules.process.processes import person_counter_process
# from database.connector.connector_postgre import PersonDatabase, CameraDatabase

# import json


# import time
# import random

# import cv2

# def check_cam(cam_url):
#     cap = cv2.VideoCapture(cam_url)

#     if not cap.isOpened():
#         return False

#     ret, frame = cap.read()

#     cap.release()

#     if ret:
#         return True
#     else:
#         return False


# def run_task(cam_url):
#     schedule = config.setting.schedule.schedule_config

#     for phase, settings in schedule.items():
#         time_minutes = settings["time"]
#         count = settings.get("count", None)  

#         if count is not None:  
#             for _ in range(count):
#                 result = check_cam(cam_url)
#                 print(f"Phase {phase}, Duration: {time_minutes} minutes, Result: {result}")
#                 time.sleep(time_minutes * 60)  

#                 if result:
#                     return True

#                 print(f"Phase {phase}, iteration {_+1}/{count} completed.")
#         else:  
#             iteration = 0
#             while True:
#                 result = check_cam(cam_url)
#                 iteration += 1
#                 print(f"Phase {phase}, Duration: {time_minutes} minutes, Result: {result}, Iteration: {iteration}")
#                 time.sleep(time_minutes * 60)  

#                 if result:
#                     return True

#     return False


# cam_url = "rtsp://minoapera:Minoa2024.@45.139.203.25:554/Streaming/Channels/101"
# cam_url = "rtsp://13.48.185.247:8554/live-stream"

# run_task(cam_url)


class_density=DensityTable()
class_density.run()