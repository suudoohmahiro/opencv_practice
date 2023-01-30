import cv2
import numpy as np

img_BGR = cv2.imread("/home/mahiroo/opencv_practice/images/candy.png")

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 50, 70])
upper_blue = np.array([112, 255, 255])
blue_mask = cv2.inRange(img_HSV, lower_blue, upper_blue)

img_blue_masked = cv2.bitwise_and(img_BGR, img_BGR, mask=blue_mask)

cv2.imshow('blue', img_blue_masked)
cv2.waitKey(0)