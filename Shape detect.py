import cv2
import numpy as np

img = cv2.imread('tri.png')
imgContour = img.copy()
# 轉灰階
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 找輪廓
canny = cv2.Canny(img, 150, 200)
# 偵測輪廓
# contours:二進位制或灰度影象 hierarchy:定義輪廓層次結構的檢索模式
# cv2.RETR_LIST:檢索所有輪廓
# cv2.RETR_EXTERNAL:僅檢索外部計數器
# cv2.RETR_COMP:檢索2級層次結構中的輪廓
# cv2.RETR_TREE:檢索完整層次結構中的輪廓
# cv2.CHAIN_APPROX_NONE:儲存所有邊界點
# cv2.CHAIN_APPROX_SIMPLE:儲存起點和終點輪廓
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("there are " + str(len(contours)) + " contours")

# cv2.draeContours(image, contours, contourIdx, color, thickness)
# contourIdx = Parameter indicating a contour to draw. If it is negative, all the contours are drawn
for cnt in contours:
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)
    area = cv2.contourArea(cnt)  # 求面積
    print('there are' + str(len(cnt)) + 'points in the contour')
    if area > 100:  # 過濾皂點
        # print(cv2.arcLength(cnt, True))
        peri = cv2.arcLength(cnt, True)  # 求周長
        # 多邊形近似輪廓
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
        corners = len(vertices)
        print(corners)
        # 用正方形包住
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 4)
        # 判斷形狀
        if corners == 6:
            cv2.putText(imgContour, 'triangle', (x, y-1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 4:
            cv2.putText(imgContour, 'rectangle', (x, y - 1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 5:
            cv2.putText(imgContour, 'pentagon', (x, y - 1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners > 6:
            cv2.putText(imgContour, 'circle', (x, y - 1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


cv2.imshow('img', img)
cv2.imshow("canny", canny)
cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)