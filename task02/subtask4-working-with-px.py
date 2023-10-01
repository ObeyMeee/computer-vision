import cv2

picture = cv2.imread("02.jpg", 1)
cv2.imshow("Initial picture", cv2.resize(picture, (int(picture.shape[1] * .5), int(picture.shape[0] * .5)),
                                       interpolation=cv2.INTER_AREA))
print(picture.shape)
px = picture[72, 52]
print(px)
blue = picture[72, 52, 0]
print(blue)
cv2.waitKey(0)
cv2.destroyAllWindows()
