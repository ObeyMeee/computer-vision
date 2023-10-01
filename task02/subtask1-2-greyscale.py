import cv2


def display_image(window_name, flag):
    picture = cv2.imread('02.jpg', flag)
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, cv2.resize(picture, (int(picture.shape[1] * 50 / 100), int(picture.shape[0] * 50 / 100)), interpolation=cv2.INTER_AREA))

    if flag == cv2.IMREAD_GRAYSCALE:
        cv2.imwrite('new02.jpg', picture)


display_image('Grayscale', cv2.IMREAD_GRAYSCALE)
display_image('Original picture', cv2.IMREAD_COLOR)
cv2.waitKey(0)
cv2.destroyAllWindows()
