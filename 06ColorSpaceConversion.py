import cv2
import numpy as np

img = cv2.imread('./img/wing_wall.jpg')

# bgr을 yuv로 변환
imgy = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
y, u, v = cv2.split(imgy)

cv2.imshow("asd", img[:,:,:])
cv2.imshow("imgy", y)
cv2.waitKey()
cv2.destroyAllWindows()

imgyy = np.full((293, 406), 255, dtype=np.uint8)
b,g,r = cv2.split(img)
imgyy = 0.299 * r + 0.587 * g + 0.114 * b
imgyy = imgyy.astype(np.uint8)

diff = y - imgyy

print(diff)
cv2.imshow('imgyy', imgyy)
cv2.imshow('diff',diff)
cv2.waitKey()
cv2.destroyAllWindows()

