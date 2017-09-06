#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('../images/shapes_donut.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grayscale, 100, 200)
image1, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(image, contours, -1, (0,255,0), 3)

cv2.imshow('contours', image)
cv2.imshow('edges', edges)
cv2.waitKey()
cv2.destroyAllWindows()
