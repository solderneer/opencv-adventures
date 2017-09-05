#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')
greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', greyscale)
cv2.waitKey()

ret ,thresh1 = cv2.threshold(greyscale, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('binary', thresh1)
cv2.waitKey()
cv2.destroyAllWindows()
