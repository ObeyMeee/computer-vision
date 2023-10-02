import cv2

ddepth = cv2.CV_16S
kernel_size = 3
window_name = 'Laplace'
window_name_original = 'Original'
fileName = '02.png'
src = cv2.imread(cv2.samples.findFile(fileName), cv2.IMREAD_COLOR)
dsize = (int(src.shape[1] * .5), int(src.shape[0] * .5))
shrunk_image = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
cv2.imshow(window_name_original, shrunk_image)
src = cv2.GaussianBlur(shrunk_image, (3, 3), 0)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
dst = cv2.Laplacian(src_gray, ddepth, ksize=kernel_size)
abs_dst = cv2.convertScaleAbs(dst)
cv2.imshow(window_name, abs_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
