import cv2

img = cv2.imread('02.jpg')
rows = img.shape[0]
columns = img.shape[1]
M = cv2.getRotationMatrix2D((columns / 2, rows / 2), 20, 1)  # Поворот на 20 градусів
dst = cv2.warpAffine(img, M, (columns, rows))
cv2.imshow('img', dst)
cv2.waitKey(0)
