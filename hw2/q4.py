import numpy as np, cv2

def onChange(value):
    global win_img, result_img, title

    alpha = cv2.getTrackbarPos('img1', title) / 100
    beta = cv2.getTrackbarPos('img2', title) / 100

    result_img = cv2.addWeighted(add_img1, alpha, add_img2, beta, 0)
    win_img[0:h, w:w*2] = result_img

    cv2.imshow(title, win_img)

add_img1 = cv2.imread("img/add_img1.jpg", cv2.IMREAD_GRAYSCALE)
add_img2 = cv2.imread("img/add_img2.jpg", cv2.IMREAD_GRAYSCALE)
if add_img1 is None or add_img2 is None: raise Exception("영상 파일 읽기 오류 발생")

result_img = cv2.addWeighted(add_img1, 0.5, add_img2, 0.5, 0)

w, h = add_img1.shape
win_img = np.zeros((w, h*3), np.uint8)
win_img[:, 0: w] = add_img1
win_img[:, w*2:] = add_img2
win_img[:, w:w*2] = result_img

title = 'dst'

cv2.imshow(title, win_img)

cv2.createTrackbar('img1', title, 50, 100, onChange)
cv2.createTrackbar('img2', title, 50, 100, onChange)

cv2.waitKey(0)