
import numpy
import random
from ultralytics import YOLO
import cv2
# coco data set class reading
my_file = open('media/coco.txt', 'r')
data= my_file.read()
class_list= data.split('\n')
my_file.close()

# Generate random colors for class list
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

model = YOLO('media/yolov8n.pt','v8')

frame_wid = 640
frame_hyt = 480

def predict_(frame):
    detect_params = model.predict(source=[frame],conf=0.45,save=False)
    DP = detect_params[0].cpu().numpy()
    result=[]
    if len(DP) != 0:
        for i in range(len(detect_params[0].cpu())):

            boxes = detect_params[0].boxes.cpu()
            box = boxes[i].cpu()  # returns one box
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]

            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsID)],
                3,
            )

            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )

            result.append(class_list[int(clsID)])

    return frame , result
    
    



