# 얼굴 인식 후 모자이크
# opencv harr filter을 연속 적용
# 2025.10.1

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')

img = cv2.imread('./img/test.png')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray)

for i in faces:
    cv2.rectangle(img, (i[0], i[1]), (i[0]+i[2], i[1]+i[3]), (255,0,0), 1)

    roi = img[i[1]: i[1]+i[3], i[0]:i[0]+i[2]]
    roi = cv2.resize(roi, (i[2]//10, i[3]//10))
    roi = cv2.resize(roi, (i[2], i[3]))

    img[i[1]: i[1]+i[3], i[0]:i[0]+i[2]] = roi

pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
font_path = "C:/Windows/Fonts/malgun.ttf"

draw = ImageDraw.Draw(pil_image)
font = ImageFont.truetype(font_path, 24)
draw.text((1250, 600), "10.01 우정광 얼굴검출", font=font, fill=(255, 0, 0))
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

