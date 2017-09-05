#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('images/input.jpg')

height, width = image.shape[:2]

t_matrix = np.array([[1,0,width/4],[0,1,height/4]], np.float32)

dst = cv2.warpAffine(image, t_matrix, (height, width))
cv2.imshow("translate", dst)

M = cv2.getRotationMatrix2D((height/2,width/2), 90, 1)
dst2 = cv2.warpAffine(image, M, (height, width))
cv2.imshow('rotate', dst2);



cv2.waitKey()
cv2.destroyAllWindows()

