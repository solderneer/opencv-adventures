#!/usr/bin/env python
import cv2
import numpy as np
from sklearn.preprocessing import scale


image = cv2.imread('images/WaldoBeach.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Beach', gray)
cv2.waitKey()
gray = scale(gray, axis=0, with_mean=True, with_std=True, copy=True)

template = cv2.imread('images/waldo.jpg')
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow('Waldo', gray_template)
cv2.waitKey()
gray_template = scale(gray, axis=0, with_mean=True, with_std=True, copy=True)

dst = cv2.filter2D(gray,-1,gray_template)

print(dst)
cv2.imshow('Where is Waldo?', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
