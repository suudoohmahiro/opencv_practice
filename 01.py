import cv2


img = cv2.imread('apple.png')

cv2.rectangle(img, (500, 400), (600, 600), (0, 255, 0), thickness=-1)
cv2.line(img, (200, 50), (200, 400), (0, 0, 255), thickness=4, lineType=cv2.LINE_AA) 
cv2.arrowedLine(img, (100, 650), (1000, 650), (255, 255, 0), thickness=4)
cv2.circle(img, (900, 1000), 60, (0, 128, 64), thickness=-1)
cv2.circle(img, (240, 700), 90, (255, 128, 0), thickness=3, lineType=cv2.LINE_AA)

cv2.imshow('sample', img)
cv2.waitKey(0)