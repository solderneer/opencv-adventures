#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('../images/someshapes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

contours = contours[1:]
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)

    if len(approx) == 3:
        shape_name = 'triangle'
        cv2.drawContours(image,[cnt], -1, (0,255,0), -1)
        M = cv2.moments(approx)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print(shape_name)
        cv2.putText(image,shape_name,(cx-50,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, 1)
    elif len(approx) == 4:
        cv2.drawContours(image, [cnt], -1, (0,0,255), -1)
        x,y,w,h = cv2.boundingRect(cnt)

        if (w-h)<3:
            shape_name = 'square'
            M = cv2.moments(approx)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            shape_name = 'rectangle'
            M = cv2.moments(approx)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

        cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)
        print(shape_name)
    elif len(approx)>15:
        cv2.drawContours(image, [cnt], -1, (255,0,0), -1)
        shape_name = 'circle'
        M = cv2.moments(approx)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)

        print(shape_name)
    elif len(approx)==10:
        cv2.drawContours(image, [cnt], -1, (125,125,0), -1)
        shape_name = 'star'

        M = cv2.moments(approx)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)

        print(shape_name)
    cv2.imshow('contours', image)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()
