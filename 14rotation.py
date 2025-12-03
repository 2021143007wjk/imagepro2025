# 2025.11.19 회전변환
import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
rows, cols = img.shape[0:2]


d90 = 90.0 * np.pi / 180
d10 = 10.0 * np.pi / 180
d45 = 45.0 * np.pi / 180


m90 = np.float32([[np.cos(d90), -np.sin(d90), rows],
                  [np.sin(d90), np.cos(d90), 0]])

m10 = np.float32([[np.cos(d10), -np.sin(d10), cols/9],
                  [np.sin(d10), np.cos(d10), 0]])
m45 = np.float32([[np.cos(d45), -np.sin(d45), cols/2],
                  [np.sin(d45), np.cos(d45), 0]])
print(d90)
print(m90)

r90 = cv2.warpAffine(img, m90, (cols, rows))
r10 = cv2.warpAffine(img, m10, (cols, rows))
r45 = cv2.warpAffine(img, m45, (cols, rows))
print(m90)

cv2.imshow('org', img)
cv2.imshow('d90', r90)
cv2.imshow('d45', r45)
cv2.imshow('d10', r10)
cv2.waitKey()
cv2.destroyAllWindows()
