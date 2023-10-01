import cv2
from matplotlib import pyplot as plt

img = cv2.imread('02.jpg', cv2.IMREAD_COLOR)
imag = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(221)
plt.imshow(imag)
plt.axis('off')
gray_img = cv2.imread('02.jpg', cv2.IMREAD_GRAYSCALE)

im_bw = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)[1]
plt.subplot(222)
plt.imshow(im_bw, 'gray')
plt.axis('off')

im_bwa = cv2.threshold(imag, 128, 255, cv2.THRESH_BINARY)[1]
plt.subplot(223)
plt.imshow(im_bwa)
plt.axis('off')

im_bwb = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV)[1]
plt.subplot(224)
plt.imshow(im_bwb, 'gray')
plt.axis('off')

plt.show()
cv2.waitKey(0)
