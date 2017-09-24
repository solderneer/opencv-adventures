#!/usr/bin/env python
import cv2
import numpy as np

template = cv2.imread('images/template-ruijie.png')
scene = cv2.imread('images/scene-ruijie.png')

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(template,None)
kp2, des2 = sift.detectAndCompute(scene, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
matchesMask = [[0,0] for i in xrange(len(matches))]
print matches

for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i] = [1,0]

draw_params = dict(matchColor = (0,255,0), singlePointColor = (255,0,0), matchesMask = matchesMask, flags = 0)

img3 = cv2.drawMatchesKnn(template,kp1,scene,kp2,matches,None,**draw_params)
cv2.imshow('matched', img3)
cv2.waitKey()
cv2.destroyAllWindows()
