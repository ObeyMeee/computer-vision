import cv2

img = cv2.imread('02.jpg')
# Перший спосіб
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
print('Resized Dimensions: ', resized.shape)
cv2.imshow('1 way to resize image', resized)
cv2.waitKey(0)

# Другий спосіб
print('Original Dimensions:', img.shape)
width = 158
height = 171
dim1 = (width, height)
# resize image
resized1 = cv2.resize(img, dim1, interpolation=cv2.INTER_AREA)
print('Resized Dimensions: ', resized1.shape)
cv2.imshow('2 way to resize image', resized1)
cv2.waitKey(0)

# Третій спосіб
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
res2 = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
cv2.imshow('img', img)
cv2.imshow('3 way to resize image', res2)
cv2.waitKey(0)
