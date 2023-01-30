import cv2
import numpy as np

img = cv2.imread("/home/mahiroo/opencv_practice/images/bananas.png")

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([15, 50, 70])
upper_yellow = np.array([45, 255, 255])
yellow_mask = cv2.inRange(img_HSV, lower_yellow, upper_yellow)

contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours = list(filter(lambda x: cv2.contourArea(x) > 100, contours))

cv2.drawContours(img, contours, -1, color=(0, 0, 255), thickness=5) #thicness を負の値にすると輪郭内部が塗りつぶされる

cv2.imshow('image', img)
cv2.waitKey(0)