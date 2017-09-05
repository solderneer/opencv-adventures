#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')

# smaller = cv2.pyrUp(image)
# bigger = cv2.pyrDown(image)
# 
# cv2.imshow('smaller', smaller)
# cv2.imshow('bigger', bigger)
# 
# cv2.waitKey()
# cv2.destroyAllWindows()

height, width = image.shape[:2]
start_row, start_col = int(height*0.25), int(width*0.25)
end_row, end_col = int(height*0.75), int(width*0.75)

crop = image[start_row:end_row, start_col:end_col]

cv2.imshow('cropped', crop)
cv2.waitKey()
cv2.destroyAllWindows()
