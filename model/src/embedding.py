import cv2
import numpy as np

class Embedding(object):
    def __init__(self, config, data):
        self.config = config
        self.data = data

    def detect_face(self, image):
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faceCascade = cv2.CascadeClassifier(self.config.cascade_path + "/" + self.config.cascade)
        faces = faceCascade.detectMultiScale(gray_scale, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
        return faces



