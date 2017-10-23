#!/usr/bin/env python
import cv2
import numpy as np
from sklearn.preprocessing import scale
import operator

def convolve2D(image_mat, filter_mat):
    # First add boundary to image

    row, column = filter_mat.shape
    reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)

image = cv2.imread('images/WaldoBeach.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Beach', gray)
cv2.waitKey()
gray_normal = scale(gray, axis=0, with_mean=True, with_std=True, copy=True)

template = cv2.imread('images/waldo.jpg')
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow('Waldo', gray_template)
cv2.waitKey()
gray_template_normal = scale(gray_template, axis=0, with_mean=True, with_std=True, copy=True)

dst = cv2.filter2D(gray_normal,-1,gray_template_normal)
indices = np.where(dst == dst.max())

print(indices)

img = cv2.circle(image,indices,63,(0,0,255),3)
cv2.imshow('Where is Waldo?', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
