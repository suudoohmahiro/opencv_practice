import cv2

img = cv2.imread("/home/mahiroo/opencv_practice/images/apple.png")

img_f = cv2.flip(img, flipCode = 1)

cv2.imshow('sample', img_f)
cv2.waitKey(0)