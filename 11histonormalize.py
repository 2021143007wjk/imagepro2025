import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('./img/yate.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])

# 이미지 노멀라이즈

# 분자 오버플로우 에러
# img_norm = ((img - img.min())*255) / (img.max() - img.min())

# 형변환 유도
# img_norm = ((img - img.min() *255.0) / (img.max() - img.min()))

#직접 형변환한 노멀라이즈
img_f = img.astype(np.float32)
img_norm = (img_f - img_f.min()) *255.0 / (img_f.max() - img_f.min())
img_norm = img_norm.astype(np.uint8)

img_normcv = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 255])
hist_normcv = cv2.calcHist([img_normcv], [0], None, [256], [0, 255])

# histogram equalize

img_eq = cv2.equalizeHist(img)
hist_eq = cv2.calcHist([img_eq],[0], None, [256], [0, 255])

plt.subplot(1,4,1)
plt.plot(hist)
plt.subplot(1,4,2)
plt.plot(hist_normcv)
plt.subplot(1,4,3)
plt.plot(hist_norm)
plt.subplot(1,4,4)
plt.plot(hist_eq)
plt.show()

cv2.imshow('imgnorm', img_norm)
cv2.imshow('eq', img_eq)
cv2.imshow('org', img)
cv2.imshow('imgnormcv', img_normcv)

cv2.waitKey()
cv2.destroyAllWindows()

# plt.plot(hist)
# plt.show()

