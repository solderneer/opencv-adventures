#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('../images/shapes.jpg')

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grayscale, 50, 200)
cv2.imshow('canny', edges)
cv2.waitKey()

image1, contours, hirarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

image = cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow('contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


