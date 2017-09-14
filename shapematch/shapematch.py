#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('../images/someshapes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow('contours', image)

cv2.waitKey()
cv2.destroyAllWindows()
