import cv2

#img_str = "/home/mahiroo/opencv_practice/images/apple.png"
img = cv2.imread("/home/mahiroo/opencv_practice/images/earth.png")
print(type(img))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('sample', hsv)
cv2.waitKey(0)