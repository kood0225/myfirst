import cv2
import numpy as np
# 創建全黑圖片 np.zeros(shape, dtype)
img = np.zeros((600, 600, 3), np.uint8)

# draw a line
# cv2.line(image, start_point, end_point, colors, thickness)
cv2.line(img, (0, 0), (400, 300), (0, 255, 0), 2)
# other method
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)

# draw a rectangle
# cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255), cv2.FILLED)
# other method
cv2.rectangle(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 2)

# draw a circle
# cv2.circle(image, center_coordinates, radius, colors, thickness)
cv2.circle(img, (300, 400), 30, (255, 0, 0), 4)
cv2.circle(img, (400, 400), 30, (255, 0, 0), cv2.FILLED)

# draw a text string on image cv2.putText(image, text, org, font, fontScale, color, thickness)
# org: It is the coordinates of the bottom-left corner of the text string in the image
cv2.putText(img, 'Hello', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)






cv2.imshow('img', img)
cv2.waitKey(0)
