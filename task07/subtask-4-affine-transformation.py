import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("02.jpg")

rows = img.shape[0]
columns = img.shape[1]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[60, 40], [200, 50], [30, 140]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, dsize=(columns, rows))
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
cv2.waitKey(0)
