
print("1")
from ultralytics import YOLO
import cv2
import os
from config.config_manager import config
import sys
from modules.detect.gender.gender import get_pred_gender

# from modules.detect.gender.gender import get_pred_gender
print("2")
model_name, model_type = config.setting.model.detect["person"].values()
model_path = os.path.join('modules/detect/person/model', f"{model_name}.{model_type}")
y_model = YOLO(model_path).to(device="cpu")

video_path = "tests/video/passage.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Couldn't open video.")
    sys.exit(1)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(5)
def main():
    frame_count=0
    frame_skip=1
    while True:
        ret, frame = cap.read()

        if not ret:
            break
        if frame_count % frame_skip == 0:

            results = y_model.track(
                    frame, conf=0.3, iou=0.5, persist=True, show=False, verbose=False
                )
            for r in results:
                boxes = r.boxes
                        
                #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                for box in boxes:
                    cls = int(box.cls[0])

                    if cls == 0:
                        x1, y1, x2, y2 = box.xyxy[0]
                        x1, y1, x2, y2 = (
                                    int(x1),
                                    int(y1),
                                    int(x2),
                                    int(y2),
                                )

                    
                    # try:
                        
                    gender_pred=get_pred_gender(frame,x1,y1,x2,y2)
                    print(gender_pred)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), thickness=5)
                    cv2.putText(frame, f"G:{gender_pred}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        
                    # except:
                        # print("Hata")
        frame_count += 1
        
        #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
if __name__=="__main__": 
    main()