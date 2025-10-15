import cv2
import numpy as np

img = cv2.imread('./img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

thresh_np = np.zeros_like(img)

thresh_np[img > 192] = 255
thresh_np[(img > 128) & (img < 192)] = 128
thresh_np[(img > 64) & (img < 128)] = 64

thresh_np2 = np.zeros_like(img)
thresh_np2[img > 64] = 64
thresh_np2[(img > 128)] = 128
thresh_np2[(img > 192)] = 192

thresh_np3 = np.zeros_like(img)
print(img.shape)
xsize, ysize = img.shape
for x in range(xsize):
    for y in range(ysize):
        if(img[x, y] > 64):
            thresh_np3[x,y] = 64
        if(img[x, y] > 128):
            thresh_np3[x,y] = 128
        if(img[x, y] > 192):
            thresh_np3[x,y] = 255

_, thresh_np4 = cv2.threshold(img, 64, 255, cv2.THRESH_BINARY)

cv2.imshow("thresh_np", thresh_np)
cv2.imshow("thresh_np2", thresh_np2)
cv2.imshow("thresh_np3", thresh_np3)
cv2.imshow("thresh_np4", thresh_np4)
cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('./img/scaned_paper.jpg',cv2.IMREAD_GRAYSCALE)
_, thresh_cv1 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
_, thresh_cv2 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, thresh_cv3 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
_, thresh_cv4 = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
t, thresh_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow("paper", img)
cv2.imshow("thresh_cv1", thresh_cv1)
cv2.imshow("thresh_cv2", thresh_cv2)
cv2.imshow("thresh_cv3", thresh_cv3)
cv2.imshow("thresh_cv4", thresh_cv4)
cv2.imshow("thresh_otsu", thresh_otsu)

print(t)

cv2.waitKey()
cv2.destroyAllWindows()

blk_size = 9
C = 5
img = cv2.imread('./img/sudoku.png', cv2.IMREAD_GRAYSCALE)
t, thresh_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blk_size, C)

cv2.imshow("img", img)
cv2.imshow("thresh_otsu", thresh_otsu)
cv2.imshow("thresh_gau", th2)
cv2.imshow("thresh_mean", th3)

print(t)

cv2.waitKey()
cv2.destroyAllWindows()
