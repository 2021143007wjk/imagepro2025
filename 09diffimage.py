import cv2
import numpy as np
img1 = cv2.imread('./img/robot_arm1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./img/robot_arm2.jpg', cv2.IMREAD_GRAYSCALE)

diff = img2 - img1
diffcv = cv2.absdiff(img1, img2)

t, diff_otsu = cv2.threshold(diffcv, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('diff', diff)
cv2.imshow('diffcv', diffcv)
cv2.imshow('diff_ots', diff_otsu)
print(f'{t=}')

cv2.waitKey()
cv2.destroyAllWindows()
