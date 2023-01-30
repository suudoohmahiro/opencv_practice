import cv2
import numpy as np

img_BGR = cv2.imread("/home/mahiroo/opencv_practice/images/candy.png")

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 70])
upper_red = np.array([9, 255, 255])
red_mask1 = cv2.inRange(img_HSV, lower_red, upper_red)

lower_red = np.array([159, 50, 70])
upper_red = np.array([179, 255, 255])
red_mask2 = cv2.inRange(img_HSV, lower_red, upper_red)

red_mask = red_mask1 | red_mask2

img_red_masked = cv2.bitwise_and(img_BGR, img_BGR, mask=red_mask)

cv2.imshow('red', img_red_masked)
cv2.waitKey(0)