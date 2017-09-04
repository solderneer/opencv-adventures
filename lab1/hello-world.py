import cv2
import numpy as np

input = cv2.imread('../images/input.jpg')

cv2.imshow("Hello World", input)

cv2.waitKey()
cv2.destroyAllWindows()
