# 얼굴 인식
# opencv harr filter을 연속 적용
# 2025.10.1

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')

img = cv2.imread('./img/test.png')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray)
eyes = eye_cascade.detectMultiScale(gray)
# [[143  95 121 121]
#  [401 100 103 103]]

# [[142 133 370 370]]
# print(faces)

# cv2.rectangle(img, (143, 95), (143+121, 95+121), (255,0,0), 5)
# cv2.rectangle(img, (401, 100), (401+103, 100+103), (0,255,0), 5)

# cv2.rectangle(img, (142, 133), (142+370, 133+370), (255,0,0), 5)

for i in faces:
    cv2.rectangle(img, (i[0], i[1]), (i[0]+i[2], i[1]+i[3]), (255,0,0), 1)

    eyes = eye_cascade.detectMultiScale(gray[i[1]: i[1]+i[3], i[0]:i[0]+i[2]])
    for j in eyes:
        cv2.rectangle(img, (i[0]+j[0], i[1]+j[1]), (i[0]+j[0]+j[2], i[1]+j[1]+j[3]), (0,0,255), 1)

pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
font_path = "C:/Windows/Fonts/malgun.ttf"

draw = ImageDraw.Draw(pil_image)
font = ImageFont.truetype(font_path, 24)
draw.text((1250, 600), "10.01 우정광 얼굴검출", font=font, fill=(255, 0, 0))
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

