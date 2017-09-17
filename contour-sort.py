#!/usr/bin/env python
import cv2
import numpy as np

def contour_area(contours):
    areas = []
    for cnt in contours:
        areas.append(cv2.contourArea(cnt))

    return areas

image = cv2.imread('../images/bunchofshapes.jpg')

cv2.imshow('original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 100, 200)
image_ret, contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(contour_area(contours))

sorted(contours, key=cv2.contourArea, reverse=True)

for cnt in contours:
    cv2.drawContours(image,cnt,-1,(0,255,0),3)
    cv2.imshow('contour', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
