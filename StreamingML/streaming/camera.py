
import cv2,os,urllib.request
import numpy as np
from django.conf import settings



class camera1:
	def __init__(self):
		pass
        # Define the codec and create VideoWriter object
	def __del__(self):
		self.video.release()
    
	def get_frame(self):
		self.video = cv2.VideoCapture(0)
		success, image = self.video.read()
		self.image= cv2.resize(image,dsize=(600,600))
		cv2.waitKey(250) # or time.sleep(1/5) for frame rate 4fps
		return self.image

#camera 3

class camera2:
	def __init__(self):
		pass
        
	def __del__(self):
		self.video.release()
    
	def get_frame(self):
		
		self.video = cv2.VideoCapture(0)	
		success, image = self.video.read()
	
		image= cv2.resize(image,dsize=(600,600))
		cv2.waitKey(250) # or time.sleep(1/5) for frame rate 4fps
		return image
#Live Cam

class camera3:
	def __init__(self):
		pass
        
	def __del__(self):
		self.video.release()
    
	def get_frame(self):
		self.video = cv2.VideoCapture(0)
		success, image = self.video.read()
		self.image= cv2.resize(image,dsize=(600,600))
		cv2.waitKey(250) # or time.sleep(1/5) for frame rate 4fps
		return self.image
#Camera 4

class camera4:
	def __init__(self):
		pass
        
	def __del__(self):
		self.video.release()
    
	def get_frame(self):
		self.video = cv2.VideoCapture(0)
		success, image = self.video.read()
		image= cv2.resize(image,dsize=(600,600))
		cv2.waitKey(250) # or time.sleep(1/5) for frame rate 4fps
		return image
