import cv2

image = cv2.imread("img/cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

def Trackbar1(pos):
    global title, th1
    th1 = pos
    canny = cv2.Canny(image, th1, th2)
    cv2.imshow(title, canny)

def Trackbar2(pos):
    global title, th2
    th2 = pos
    canny = cv2.Canny(image, th1, th2)
    cv2.imshow(title, canny)

title = "canny edge"
t1 = "th1"
t2 = "th2"

th1 = 100
th2 = 150

canny = cv2.Canny(image, th1, th2)
cv2.imshow(title, canny)

cv2.createTrackbar(t1, title, th1, 255, Trackbar1)
cv2.createTrackbar(t2, title, th2, 255, Trackbar2)

cv2.waitKey(0)