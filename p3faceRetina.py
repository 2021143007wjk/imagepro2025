#2025.12.3 종강

import cv2
from PIL import ImageFont, ImageDraw, Image
from retinaface import RetinaFace
import numpy as np
img_path = "./img/test.png"

faces = RetinaFace.detect_faces(img_path)
print(faces.keys())
print(faces.values())

img = cv2.imread(img_path)
for key, face in faces.items():
    print(key)
    print(face)
    facial_area = face['facial_area']
    cv2.rectangle(img, (facial_area[0], facial_area[1]), (facial_area[2], facial_area[3]), (255, 0, 0), 2)

    cv2.putText(img, f'{face["score"]:.3f}', (facial_area[0], facial_area[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))

pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
font_path = "C:/Windows/Fonts/malgun.ttf"

draw = ImageDraw.Draw(pil_image)
font = ImageFont.truetype(font_path, 24)
draw.text((1365, 0), "우정광 제작", font=font, fill=(255, 0, 0))
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

