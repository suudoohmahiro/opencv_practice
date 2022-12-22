import cv2

img1 = cv2.imread("/home/mahiroo/opencv_practice/images/sunglasses.png")
img2 = cv2.imread("/home/mahiroo/opencv_practice/images/snowman.png")

img1_resize = cv2.resize(img1, (1280,853))
img2_resize = cv2.resize(img2, (1280,853))

img1_gray = cv2.cvtColor(img1_resize, cv2.COLOR_BGR2GRAY) 

img_add = cv2.addWeighted(img1_gray, 0.3, img2_resize, 0.7, 10)


cv2.imshow('sunglasess_snowman.png', img_add)
cv2.waitKey(0)