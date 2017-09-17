#!/usr/bin/env python
import cv2
import numpy as np

def calcXpos(contour):
    M = cv2.moments(contour)
    return (int(M['m10']/M['m00']))

image = cv2.imread('../images/shapes_donut.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grayscale, 100, 200)
image1, contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

contours = sorted(contours, key = calcXpos)

for cnt in contours:
    image = cv2.drawContours(image, cnt, -1, (0,255,0),3)
    cv2.imshow('contours', image)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()
