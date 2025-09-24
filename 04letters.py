import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = np.full((500, 500, 3), 255, dtype=np.uint8)

cv2.putText(img, "plain", (50,30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))

cv2.putText(img, "simplex", (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))

cv2.putText(img, "duplex", (50,110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))

cv2.putText(img, "simplex2", (200,110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0))



cv2.putText(img, "serif plain", (50,180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))

cv2.putText(img, "serif normal", (50,220), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))

cv2.putText(img, "serif bold", (50,260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))

cv2.putText(img, "serif palin2", (50,320), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0))

pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
font_path = "C:/Windows/Fonts/malgun.ttf"

draw = ImageDraw.Draw(pil_image)
font = ImageFont.truetype(font_path, 24)
draw.text((50, 470), "우정광 제작", font=font, fill=(255, 0, 0))
img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

cv2.imshow("wing_wall", img)
cv2.waitKey()
cv2.destroyAllWindows()
