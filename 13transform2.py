import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
rows, cols, _ = img.shape

mtrx_filpx = np.float32([[-1, 0, cols], [0,1,0]])
mtrx_filpy = np.float32([[1, 0, 0], [0,-1,rows]])
mtrx_filpxy = np.float32([[-1, 0, cols], [0,-1,rows]])

img1 = cv2.warpAffine(img, mtrx_filpx, (cols, rows))
img2 = cv2.warpAffine(img, mtrx_filpy, (cols, rows))
img3 = cv2.warpAffine(img, mtrx_filpxy, (cols, rows))

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()

#좌우 반전을 파이썬 프로그램으로
img_flipx =np.zeros_like(img)

for x in range(cols):
    for y in range(rows):
        # img_flipx[x,y] = img[cols-x-1, y] # x,y가 반대라 상하 반전이 됨
        img_flipx[y,x] = img[y, cols-x-1] # x,y가 반대라 상하 반전이 됨

array_flipx = np.zeros_like(img)
for x in range(cols):
    array_flipx[:, x] = img[:, cols-x-1]

img_flipy = np.zeros_like(img)
for x in range(cols):
    for y in range(rows):
        img_flipy[y,x] = img[rows -y -1, x]

cv2.imshow('flipx', img_flipx)
cv2.imshow('flipy', img_flipy)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
# 회전전화병렬
# 대칭변환행렬
#