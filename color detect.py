import cv2
import numpy as np

def empty(v):
    pass

img = cv2.imread('ppp.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Create a window with a suitable name and size to display images and videos on the screen.
cv2.namedWindow('TrackBar')
# Resize window displaying images to a specific size.
# cv2.resizeWindow(window_named, width, height)
cv2.resizeWindow('TrackBar', 640, 320)
# Create a Trackbar to control HSV
cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

# transfer to HSV type
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar') # getTrackbarPos(Trackbar_name, window)
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min]) # np.array() --> create an array
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper) # 過濾顏色
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(1)

