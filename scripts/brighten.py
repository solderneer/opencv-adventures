#!/usr/bin/env python

import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')

factor = np.ones(image.shape, dtype = 'uint8') * 75

added = cv2.add(image, factor)
subtract = cv2.subtract(image, factor)

cv2.imshow('Add', added)
cv2.imshow('Subtract', subtract)

cv2.waitKey()
cv2.destroyAllWindows()

