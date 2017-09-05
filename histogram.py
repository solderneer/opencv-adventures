#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt

input = cv2.imread('image/input.jpg')

color = ('b','g','r')

for i in enumerate(color):
    histogram = cv2.calcHist([input], [i], None, [256], [0,256])
    plt.hist(histogram, color = col)
    plt.xlim([0,256])

plt.show()

