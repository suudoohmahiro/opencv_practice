import cv2

img = cv2.imread("/home/mahiroo/opencv_practice/images/aozora.png")

height = img.shape[0]
width = img.shape[1]

img2 = cv2.resize(img , (int(width*1.2), int(height*1.2)))

img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', img_gray)
cv2.waitKey(0)