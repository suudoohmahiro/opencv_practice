import cv2
import numpy as np

img_BGR = cv2.imread("/home/mahiroo/opencv_practice/images/candy.png")

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)

lower_green = np.array([40, 75, 75])
upper_green = np.array([80, 255, 255])
green_mask = cv2.inRange(img_HSV, lower_green, upper_green)

img_green_masked = cv2.bitwise_and(img_BGR, img_BGR, mask=green_mask)

cv2.imshow('green', img_green_masked)
cv2.waitKey(0)