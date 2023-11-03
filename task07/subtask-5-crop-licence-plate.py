import cv2
import numpy as np

img = cv2.imread("02.jpg")

x_center = 850
y_center = 485
center = (x_center, y_center)
rect_length = 162
rect_height = 60
size = (rect_length, rect_height)
angle = -10
rect_pts = cv2.boxPoints(((center[0], center[1]), (size[0], size[1]), angle))
cv2.drawContours(img, [np.intp(rect_pts)], 0, (0, 0, 255), 3)
cv2.imshow("Image", img)
x_crop_start = (x_center - rect_length / 2).__round__()
x_crop_end = (x_center + rect_length / 2).__round__()
y_crop_start = (y_center - rect_height / 2).__round__()
y_crop_end = (y_center + rect_height / 2).__round__()
crop = img[y_crop_start:y_crop_end, x_crop_start: x_crop_end]
piece = cv2.resize(crop, dsize=(200, 50), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Area", piece)
(h, w) = piece.shape[:2]
print(w, h)
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, angle=90, scale=2.0)
rotated = cv2.warpAffine(piece, M, dsize=(300, 150))
cv2.imshow("Rotated", rotated)
cv2.waitKey()
