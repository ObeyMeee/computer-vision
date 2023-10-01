import cv2


def display_image(window_name, flag):
    picture = cv2.imread('new02.jpg', flag)
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, cv2.resize(picture, (int(picture.shape[1] * 50 / 100), int(picture.shape[0] * 50 / 100)),
                                       interpolation=cv2.INTER_AREA))
    return picture


picture = display_image('Grayscale', cv2.IMREAD_GRAYSCALE)
print(type(picture)) # Клас ==> <class 'numpy.ndarray'>
print(picture.shape) # Кортеж числа рядків та стовпців, і каналів RGB (768, 1024)
print(picture.size) # Кількість пікселів 786432
print(picture.dtype) # Тип даних зображення ==> uint8
cv2.waitKey(0)
cv2.destroyAllWindows()
