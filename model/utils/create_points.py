import cv2
import numpy as np
import json
#from ..config import config

points = []

def replace_source_in_config(file_path, camera_id, points):
    with open(file_path, "r") as file:
        config = json.load(file)

    config["setting"]["processing"]["source"][camera_id]["point_data"]["points"] = points

    # print(config["setting"]["processing"]["source"][camera_id]["point_data"]["points"])

    with open(file_path, "w") as file:
        json.dump(config, file, indent=4)


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(frame,(x,y),5,(255,0,0),-1)
        points.append((x, y))

camera_id = "10"
#video_path = config.setting.processing.source[camera_id]["video_path"]
video_path = "rtsp://minoa:Minoa2024.@45.139.203.25:554/Streaming/Channels/1301"

cap = cv2.VideoCapture(video_path)

while True:
    success, frame = cap.read()
    if not success:
        break

    cv2.namedWindow('Webcam')
    cv2.setMouseCallback('Webcam', draw_circle)

    if len(points) >= 2:
        cv2.polylines(frame,[np.array(points)],True,(0,255,255))
        points_array = np.array(points)
        center_point = points_array.mean(axis=0)

    
    
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


print("="*80)
print(points)
print("="*80)

file_path = "config/json/config.json"
replace_source_in_config(file_path=file_path,camera_id=camera_id, points=points)
