import os
import cv2
import numpy as np

class Embedding(object):
    def __init__(self, config, data):
        self.config = config
        self.data = data

    def detect_face(self, image):
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_scale = np.asarray(gray_scale, dtype='uint8')
        faceCascade = cv2.CascadeClassifier(os.path.join(self.config.cascade_path , self.config.cascade))
        faces = faceCascade.detectMultiScale(gray_scale, scaleFactor=1.08, minNeighbors=1)
        if(str(type(faces)) == "<class 'tuple'>"):
            return np.zeros((32, 32))
        return gray_scale[faces[0, 1]: faces[0, 1] + faces[0, 2], faces[0, 0]: faces[0, 0] + faces[0, 3]].shape
