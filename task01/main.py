import os

import cv2


def display_picture(picture, window_name):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, picture)
    cv2.waitKey(-1)
    cv2.destroyAllWindows()


image_file_name = os.path.join(os.getcwd(), 'task01/02.jpg')
picture = cv2.imread(image_file_name)
display_picture(picture, 'Original picture')
display_picture(picture[15:480, 480:680], 'cut picture')
pict = cv2.imread(image_file_name)
d = (int(pict.shape[1] * 50 / 100), int(pict.shape[0] * 50 / 100))
display_picture(cv2.resize(pict, d, interpolation=cv2.INTER_AREA), 'scale - 50%')
(h, w, d) = pict.shape
c = (w // 2, h // 2)
display_picture(cv2.warpAffine(pict, cv2.getRotationMatrix2D(c, 60, 1), (w, h)), 'Rotate 60 deg')
o = pict.copy()
cv2.putText(o, 'I love Computer Vision', (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 127), 5)
display_picture(o, 'Text')
