import cv2
import numpy as np
import concurrent.futures
import multiprocessing
import time
from .views import *
from .camera import *


def grid():
    while True:
        with concurrent.futures.ProcessPoolExecutor(1) as executor:
            future1=executor.submit(camera1().get_frame)
            future2=executor.submit(camera2().get_frame)
            future3=executor.submit(camera3().get_frame)
            future4=executor.submit(camera4().get_frame)

        concat_frame1= cv2.hconcat([future1.result(),future2.result()])
        concat_frame2= cv2.hconcat([future3.result(),future4.result()])
        final = cv2.vconcat([concat_frame1,concat_frame2])
        ret, jpeg = cv2.imencode('.jpg',final)

        jpeg=jpeg.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + jpeg + b'\r\n\r\n')


    
