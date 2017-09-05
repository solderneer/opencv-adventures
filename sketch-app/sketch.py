#!/usr/bin/env python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray_blur = cv2.GaussianBlur(gray, (3,3), 0)
    edges = cv2.Canny(gray, 100, 200)
    ret, thresh1 = cv2.threshold(edges, 20, 255, cv2.THRESH_BINARY_INV)
    return thresh1

while(True):
    ret, frame = cap.read()
    cv2.imshow('sketch-app', sketch(frame))
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
