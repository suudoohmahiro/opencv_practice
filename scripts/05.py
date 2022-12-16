import cv2

img = cv2.imread("/home/mahiroo/opencv_practice/images/clock.png") #614 960

cv2.putText(img, 'Time is money', (580, 300), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (0, 0, 255), thickness = 4 )

img_f = cv2.flip(img, flipCode = 1)

cv2.imwrite('/home/mahiroo/opencv_practice/images/clock_mirror.png', img_f)

cv2.imshow('time is money', img_f)
cv2.waitKey(0)