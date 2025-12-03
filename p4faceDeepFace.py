#2025.12.3 마지막 프로젝트

import cv2
from deepface import DeepFace
import numpy as np
import time
import matplotlib.pyplot as plt

img_path = "./img/children.jpg"
img = cv2.imread(img_path)
# retinaface, centerface, yunet, mtcnn, opencv, ssd
faces = DeepFace.extract_faces(img_path=img_path, detector_backend='mtcnn', enforce_detection=False)

print(faces)

for face in faces:
    facial_area = face['facial_area']
    x = facial_area['x']
    y = facial_area['y']
    w = facial_area['w']
    h = facial_area['h']
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.putText(img, f'{face["confidence"]:.3f}', (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

timing = []

backends = ['retinaface', 'centerface', 'yunet', 'mtcnn']
for engine in backends:
    img = cv2.imread(img_path)
    start = time.time()

    faces = DeepFace.extract_faces(img_path=img_path, detector_backend=engine, enforce_detection=False)

    end = time.time()
    timing.append(end-start)
print(timing)
plt.bar(backends, timing, color='skyblue', alpha= 0.7)
plt.xlabel("Engine")
plt.ylabel("time")
plt.show()