import cv2
import numpy as np

image = cv2.imread('02.jpg')
image = cv2.resize(image, (int(image.shape[1] * .5), int(image.shape[0] * .5)), interpolation=cv2.INTER_AREA)
img = image.copy()
K = 7  # 5 + 2
s = img.shape
h1, w1 = s[0], s[1]
h = (s[0] - s[1] % K)
w = (s[0] - s[1] % K)
img = cv2.resize(img, (w, h))
for y in range(0, h - 1, K):
    for x in range(0, w - 1, K):
        if len(s) > 2:
            s = np.average(img[y: (y + K), x:(x + K)], axis=0)
            img[y:(y + K), x:(x + K)] = np.average(s, axis=0)
        else:
            s = img[y:(y + K), x:(x + K)]
            img[y:(y + K), x:(x + K)] = np.average(s)
img = cv2.resize(img, (w1, h1))
res = np.hstack((image, img))
cv2.imshow('Img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
