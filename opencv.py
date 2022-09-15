import cv2
import numpy as np
#創造二維陣列
kernel = np.ones((5, 5), np.uint8)
kernel1 = np.ones((5, 5), np.uint8)


# 讀取圖片
img = cv2.imread('shishou.png')
# 縮放圖片
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# 彩色轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 高斯模糊(圖片, (奇數, 奇數), 標準差)
blur = cv2.GaussianBlur(img, (17, 17), 5)
# 邊緣圖片(圖片, 最低門檻值, 最高門檻值)
canny = cv2.Canny(img, 50, 600)
# 膨脹圖片(圖片, 核-二維陣列, 膨脹次數)
dilate = cv2.dilate(canny, kernel, iterations=1)
# 侵蝕圖片(圖片, 核-二維陣列, 侵蝕次數)
erode = cv2.erode(dilate, kernel1, iterations=1)
# 印出圖片大小
print(img.shape)



# 顯示圖片
cv2.imshow('chihaya', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
# 留住圖片
cv2.waitKey(0)


#讀取影片
import cv2
# cv2.VideoCapture(filename)
cap = cv2.VideoCapture('fgo.mp4')


while True:
    ret, frame = cap.read()  # read frame rate, ret: boolean 是否成功, frame: 若成功回傳圖片
    print(ret)
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
