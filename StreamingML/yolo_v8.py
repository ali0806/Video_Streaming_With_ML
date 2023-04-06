from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.pt", "v8")

detection_output  = model.predict(source='media/profile_pics/cat.jpg',conf=0.25,save=False)

print(detection_output)
