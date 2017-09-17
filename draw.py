#!/usr/bin/env python

import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

cv2.circle(image, (250,250), 100, (255,255,255), 5)
cv2.rectangle(image, (150,150), (350,350), (255,255,255), 5)
cv2.line(image, (150,150), (350,350), (255,255,255), 5)
cv2.line(image, (350,150), (150,350), (255,255,255), 5)
cv2.imshow("line", image)

cv2.waitKey()
cv2.destroyAllWindows()

