from ultralytics import YOLO
import cv2
import numpy as np
from ultralytics import YOLO
import requests
from io import BytesIO



class VideoPersonBlur:
    def __init__(self, model_path) -> None:
        self.model_path = model_path
        self.model = YOLO(model_path)

    def get_first_frame(self, video_url: str) -> np.array:
        cap = cv2.VideoCapture(video_url)

        ret, first_frame = cap.read()
        if not ret:
            cap.release()
            exit("Video'dan kare okunamadı.")

        cap.release()  
        return first_frame

    def get_blur_image(self, video_url):
        first_frame = self.get_first_frame(video_url)
        results = self.model(first_frame, verbose=False)

        for r in results:
            boxes = r.boxes

            for box in boxes:
                # Sınıf adı
                cls = int(box.cls[0])
                if cls == 0:  
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    face_region_height = y2 - y1
                    blur_region_height = face_region_height // 3
                    blur_y1 = y1
                    blur_y2 = y1 + blur_region_height

                    face_region = first_frame[blur_y1:blur_y2, x1:x2]
                    blurred_face = cv2.GaussianBlur(face_region, (99, 99), 0)
                    first_frame[blur_y1:blur_y2, x1:x2] = blurred_face

        return first_frame