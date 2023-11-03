import cv2
import numpy as np

img = cv2.imread('02.jpg')
rows = img.shape[0]
columns = img.shape[1]
M = np.float32([[1, 0, 40], [0, 1, 20]])  # зсув на 40 стовпців та 20 рядків
dst = cv2.warpAffine(img, M, (columns, rows))
cv2.imshow('img', dst)
cv2.waitKey(0)
