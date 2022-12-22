import cv2

img1 = cv2.imread("/home/mahiroo/opencv_practice/images/marguerite.png") #1280 833
img2 = cv2.imread("/home/mahiroo/opencv_practice/images/sunglasses.png") #1280 853

img1_resize = cv2.resize(img1, (1280,833))
img2_resize = cv2.resize(img2, (1280,833))

HSV_img1 = cv2.cvtColor(img1_resize, cv2.COLOR_BGR2HSV)

img_add = cv2.addWeighted(HSV_img1, 0.6, img2_resize, 0.4, 10)

cv2.imwrite('/home/mahiroo/opencv_practice/images/HSV_add.png', img_add)

cv2.imshow('HSV_add', img_add)
cv2.waitKey(0)