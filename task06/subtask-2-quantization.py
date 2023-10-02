import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('02.jpg')
img = cv2.resize(img, (int(img.shape[1] * .5), int(img.shape[0] * .5)), interpolation=cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.subplot(122)
Z = img.reshape((-1, 3))
Z = np.float32(Z)
crt = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret, label, center = cv2.kmeans(Z, K, None, crt, 10, cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
res3 = np.hstack((img, res2))
cv2.imshow('Img', res3)
cv2.waitKey(0)
cv2.destroyAllWindows()
