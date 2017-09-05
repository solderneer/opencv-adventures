#!/usr/bin/env python

import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')

blur = cv2.blur(image, (3,3))
gaussian_blur = cv2.GaussianBlur(image, (3,3), 0)
median = cv2.medianBlur(image, 5)

cv2.imshow("boxblux", blur)
cv2.waitKey()
cv2.imshow("gaussian", gaussian_blur)
cv2.waitKey()
cv2.imshow("median", median)
cv2.waitKey()

# should go look into image de-noising
# brighten needs an array [-1,-1,-1],[-1,9,-1],[-1,-1,-1]
# kernel/convolution matrix can even be used for edge detection
matrix = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharp = cv2.filter2D(image, -1, matrix)

cv2.imshow("sharp", sharp)
cv2.waitKey()
cv2.destroyAllWindows()
