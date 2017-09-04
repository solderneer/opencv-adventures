import cv2
import numpy as np

input = cv2.imread('../images/input.jpg')

cv2.imshow("Hello World", input)

print("The height of the image is", int(input.shape[0]))
print("The width of the image is", int(input.shape[1]))

cv2.waitKey()
cv2.destroyAllWindows()
