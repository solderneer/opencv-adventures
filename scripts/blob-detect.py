#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('../images/Sunflowers.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detector = cv2.SimpleBlobDetector()

keypoints = detector.detect(gray)
image_keyed = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255))
cv2.imshow('keyed', image_keyed)

cv2.waitKey()
cv2.destroyAllWindows()
