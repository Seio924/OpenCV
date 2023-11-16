import cv2

h = int(input('높이 : '))
w = int(input('너비 : '))

roi_h = 240
roi_w = 320

roi_x = w//2 - roi_w//2
roi_y = h//2 - roi_h//2

title = "ex11 - mainWindow"


capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

while True:
    ret, img = capture.read()

    tmp = cv2.resize(img, (roi_w, roi_h))
    img[:, :] = (255, 0, 0)
    img[roi_y - 2:roi_y + roi_h + 2, roi_x- 2:roi_x + roi_w + 2] = (0, 0, 255)
    img[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w] = tmp

    if ret:
        cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(title, img)

        cv2.resizeWindow(title, h, w)
        cv2.waitKey(33)
    else:
        break

capture.release()
cv2.destroyallWindows()