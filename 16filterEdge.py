#25.11.26
import cv2
import numpy as np

img = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)

gx_kernel = np.array([[-1,1]])
edge_gx = cv2.filter2D(img, -1, gx_kernel)
gy_kernel = np.array([[-1],[1]])
edge_gy = cv2.filter2D(img, -1, gy_kernel)


cv2.imshow('org',img)
cv2.imshow('xedge', edge_gx)
cv2.imshow('yedge', edge_gy)
cv2.waitKey()
cv2.destroyAllWindows()

# sobel
gx_s = np.array([[-1, 0, 1], [-2, 0, 2],[-1, 0, 1]])
gy_s = np.array([[-1, -2, -1], [0, 0, 0],[1, 2, 1]])
edge_gxs = cv2.filter2D(img, -1, gx_s)
edge_gys = cv2.filter2D(img, -1, gy_s)
edge_gxys = edge_gxs+ edge_gys

sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)

cv2.imshow('org',img)
cv2.imshow('xedge', edge_gxs)
cv2.imshow('yedge', edge_gys)
cv2.imshow('sobeledge', sobelx)
cv2.imshow('xyedge', edge_gxys)

cv2.waitKey()
cv2.destroyAllWindows()

# schar
gx_sh = np.array([[-3,0,3], [-10,0,10], [-3,0,3]])
gy_sh = gx_sh.T
print(gy_sh)
scharx = cv2.filter2D(img, -1, gx_sh)
schary = cv2.filter2D(img, -1, gy_sh)

#laplacian
gx_l = np.array([[0,1,0], [1,-4,1], [0,1,0]])
edge_l = cv2.filter2D(img, -1, gx_l)

#canny
canny = cv2.Canny(img, 50, 150)

cv2.imshow('org',img)
cv2.imshow('scharx', scharx)
cv2.imshow('schary', schary)
cv2.imshow('edge_l', edge_l)
cv2.imshow('canny', canny)
cv2.waitKey()
cv2.destroyAllWindows()