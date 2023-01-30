import cv2
import numpy as np

img_BGR = cv2.imread("/home/mahiroo/opencv_practice/images/candy.png")

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([25, 50, 70])
upper_yellow = np.array([35, 255, 255])
yellow_mask = cv2.inRange(img_HSV, lower_yellow, upper_yellow)

img_yellow_masked = cv2.bitwise_and(img_BGR, img_BGR, mask=yellow_mask)

cv2.imshow('yellow', img_yellow_masked)
cv2.waitKey(0)