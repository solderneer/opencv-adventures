#!/usr/bin/env python

import cv2
import numpy as np

image = imread('../images/input.jpg')

blur = cv2.blur(image, (3,3))
guassian_blur = cv2.GuassianBlur(image, (3,3), 0)
median = cv2.medianBlur(image, 5)

# should go look into image de-noising
# brighten needs an array [-1,-1,-1],[-1,9,-1],[-1,-1,-1]
matrix = np.array([],[],[])
