#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('images/WaldoBeach.jpg')
cv2.imshow('original', image)
cv2.waitKey()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('images/waldo.jpg')
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow('Waldo', gray_template)
cv2.waitKey()

result = cv2.matchTemplate(gray, gray_template, cv2.TM_CCOEFF)
cv2.imshow('Result', result)
cv2.waitKey()
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)

cv2.imshow('Where is Waldo?', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
