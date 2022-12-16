import cv2

img1 = cv2.imread("/home/mahiroo/opencv_practice/images/milkyway.png")
img2 = cv2.imread("/home/mahiroo/opencv_practice/images/aozora.png")

img1_resize = cv2.resize(img1, (1280,1000))
img2_resize = cv2.resize(img2, (1280,1000))

img_a= cv2.addWeighted(img1_resize, 0.5, img2_resize, 0.5, 2.2)

cv2.imshow('addWeighted', img_a)
cv2.waitKey(0)