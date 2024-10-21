from config import config
import time
import cv2

def check_cam(cam_url):
    cap = cv2.VideoCapture(cam_url)

    if not cap.isOpened():
        return False

    ret, frame = cap.read()

    cap.release()

    if ret:
        return True
    else:
        return False


def schedule_cam_check(cam_url):

    schedule = config.setting.schedule.schedule_config

    for phase, settings in schedule.items():
        time_minutes = settings["time"]
        count = settings.get("count", None)  

        if count is not None:  
            for _ in range(count):
                result = check_cam(cam_url)
                print(f"Phase {phase}, Duration: {time_minutes} minutes, Result: {result}")
                time.sleep(time_minutes * 60)  

                if result:
                    return True

                print(f"Phase {phase}, iteration {_+1}/{count} completed.")
        else:  
            iteration = 0
            while True:
                result = check_cam(cam_url)
                iteration += 1
                print(f"Phase {phase}, Duration: {time_minutes} minutes, Result: {result}, Iteration: {iteration}")
                time.sleep(time_minutes * 60)  

                if result:
                    return True

    return False


