import cv2
import numpy as np

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

# Зчитування
img = cv2.imread("02.jpg")

# Вирізання
x_center = 850
y_center = 485
rect_length = 162
rect_height = 85
x_crop_start = (x_center - rect_length / 2).__round__()
x_crop_end = (x_center + rect_length / 2).__round__()
y_crop_start = (y_center - rect_height / 2).__round__()
y_crop_end = (y_center + rect_height / 2).__round__()
original_licence_plate = img[y_crop_start:y_crop_end, x_crop_start: x_crop_end]

# Додавання шуму
mean = 0
stddev = 5
noise = np.random.normal(mean, stddev, original_licence_plate.shape).astype('uint8')
noisy_image = cv2.add(original_licence_plate, noise)

# Збереження отриманого зображення у монохромному вигляді
gray_img = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_img.jpg', gray_img)

# Завантаження отриманого монохромного зображення
gray_img = cv2.imread('gray_img.jpg')

# Збільшення зображення
width = int(gray_img.shape[1] * 3)
height = int(gray_img.shape[0] * 3)
gray_resized_img = cv2.resize(gray_img, (width, height), interpolation=cv2.INTER_AREA)
cv2.imshow("Gray Noisy Licence Plate", gray_resized_img)

# Застосування фільтрів
median_filtered_image = cv2.medianBlur(gray_resized_img, 7)
cv2.imshow("Median filtered image", median_filtered_image)

kernel = np.ones((5, 5), np.float32) / 25
mean_filtered_image = cv2.filter2D(gray_resized_img, -1, kernel)
cv2.imshow("Mean filtered image", mean_filtered_image)

kernel = np.ones((5, 5), np.uint8)
erode_filtered_image = cv2.erode(gray_resized_img, kernel, iterations=1)
cv2.imshow('Erode Filter', erode_filtered_image)

geometric_mean_filtered_image = rgb_geometric_mean(gray_resized_img)
cv2.imshow("Geometric mean filter", geometric_mean_filtered_image)
cv2.waitKey()
