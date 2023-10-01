import cv2
import numpy as np


def improve_image_with_median_filter(image_for_median):
    processed_image = cv2.medianBlur(image_for_median, 7)
    cv2.imshow('Median Filter', processed_image)
    cv2.imwrite('median_processed_image.png', processed_image)


def improve_image_with_mean_filter(image_for_mean):
    kernel = np.ones((5, 5), np.float32) / 25
    processed_image = cv2.filter2D(image_for_mean, -1, kernel)
    cv2.imshow('Mean Filter', processed_image)
    cv2.imwrite('mean_processed_image.png', processed_image)


def improve_image_with_erode(image_for_erode):
    kernel = np.ones((5, 5), np.uint8)
    processed_image = cv2.erode(image_for_erode, kernel, iterations=1)
    cv2.imshow('Erode Filter', processed_image)
    cv2.imwrite('erode_processed_image.png', processed_image)


image = cv2.imread('02.jpg')
dsize = (int(image.shape[1] * .5), int(image.shape[0] * .5))
shrunk_image = cv2.resize(image, dsize, interpolation=cv2.INTER_AREA)
cv2.namedWindow('Initial image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Initial image', shrunk_image)

improve_image_with_median_filter(shrunk_image)
improve_image_with_mean_filter(shrunk_image)
improve_image_with_erode(shrunk_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
