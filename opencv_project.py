# Opencv_Project: Virtual
import cv2
import numpy as np



cap = cv2.VideoCapture(0)
def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([85, 124, 100])  # np.array() --> create an array
    upper = np.array([110, 248, 255])

    mask = cv2.inRange(hsv, lower, upper)  # 過濾顏色
    result = cv2.bitwise_and(img, img, mask=mask)
    penx, peny = findcontour(mask)
    cv2.circle(imgContour, (penx, peny), 10, (255, 0, 0), cv2.FILLED)
    cv2.imshow('result', result)
def findcontour(img):
    # gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # canny = cv2.Canny(gray, 150, 200)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri*0.01, True)
            x, y, w, h = cv2.boundingRect(vertices)
    return x, y









while True:
    ret, frame = cap.read()
    if ret:
        imgContour = frame.copy()
        cv2.imshow('video', frame)
        findPen(frame)
        cv2.imshow('contour', imgContour)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break