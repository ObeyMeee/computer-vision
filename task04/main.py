import cv2
import numpy as np
import matplotlib.pyplot as plt


def geometric_mean_algorithm(image):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            roi = image[i - 1:i + 2, j - 1: j + 2]
            roi = roi.astype(np.float64)
            p = np.prod(roi)
            new_image[i - 1, j - 1] = p ** (1 / (roi.shape[0] * roi.shape[1]))
    return new_image.astype(np.uint8)


def rgb_geometric_mean(image):
    r, g, b = cv2.split(image)
    r = geometric_mean_algorithm(r)
    g = geometric_mean_algorithm(g)
    b = geometric_mean_algorithm(b)
    return cv2.merge([r, g, b])


img = cv2.imread('02.png')
image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
plt.imshow(image)
plt.title('Noisy image')
plt.show()
newImg = rgb_geometric_mean(image)
plt.imshow(newImg)
plt.title('Geometric Mean Filter')
plt.show()
