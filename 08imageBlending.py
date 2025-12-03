import cv2
import numpy as np

img1 = cv2.imread('./img/wing_wall.jpg')
img2 = cv2.imread('./img/yate.jpg')

img3 = img1 //2 + img2 //2
img4 = cv2.add(img1, img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 이미지 합성 웨이트로 처리
alpha = 0.7
blended_img = img1 * alpha + img2 * (1-alpha)
blended_img = blended_img.astype(np.uint8)

blended_cv = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)

cv2.imshow('blend', blended_img)
cv2.imshow('blend2', blended_cv)
cv2.waitKey()
cv2.destroyAllWindows()

# 가변 웨이트로 합성
img1 = cv2.imread('./img/lion_face.jpg')
img2 = cv2.imread('./img/man_face.jpg')

win_name= 'blending'
def onChgage(x):
    alpha = x /100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
    cv2.imshow(win_name, dst)


cv2.imshow(win_name, img1)
cv2.createTrackbar('fade', win_name, 0, 100, onChgage)

cv2.waitKey()
cv2.destroyAllWindows()

