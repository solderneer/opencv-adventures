#!/usr/bin/env python
import cv2
import numpy as np

input = cv2.imread('./images/input.jpg')

B, G, R = cv2.split(input)

zeros = np.zeros(input.shape[:2], dtype = "uint8")

cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))

combine = cv2.merge([B,G,R]);

cv2.imshow("Combined", combine)

cv2.waitKey()
cv2.destroyAllWindows()

