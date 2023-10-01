import cv2
import numpy as np

img = cv2.imread('02.jpg', cv2.IMREAD_COLOR)
center = (850, 485)
size = (162, 60)
angle = -10
rect_pts = cv2.boxPoints(((center[0], center[1]), (size[0], size[1]), angle))
cv2.drawContours(img, [np.intp(rect_pts)], 0, (0, 0, 255), 2)
cv2.imshow('selected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
