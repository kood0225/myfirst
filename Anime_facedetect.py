import cv2
import sys
import os.path

import numpy as np


# def face_detect(filename, cascade_file = "../lbpcascade_animeface.xml"):
img = cv2.imread('many.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('lbpcascade_animeface.xml')
faces = face_cascade.detectMultiScale(gray, 1.005, 30)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
cv2.imshow('chihaya', img)
cv2.waitKey(0)


# if __name__ == '__main__':
#     print('__name__:',  __name__)
#     face_detect('72.jpg', 'lbpcascade_animeface.xml')
