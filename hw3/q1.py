import numpy as np
import cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 0, np.uint8)  # 검은색 배경으로 초기화
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1] / hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * float(gap)))
        w = int(round(float(gap)))
        pt1 = (x, 0)
        pt2 = (x + w, 0 + int(h))
        cv2.rectangle(hist_img, pt1, pt2, 255, cv2.FILLED)  # 흰색으로 변경

    return cv2.flip(hist_img, 0)

image = cv2.imread("img/affine_test1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

# 수직 방향 투영 (열 방향 합)
vertical_projection = cv2.reduce(image, 0, cv2.REDUCE_AVG).ravel().astype(int)

# 수평 방향 투영 (행 방향 합)
horizontal_projection = cv2.reduce(image, 1, cv2.REDUCE_AVG).ravel().astype(int)


hist_img1 = draw_histo(vertical_projection)
hist_img2 = draw_histo(horizontal_projection)

hist_img2 = cv2.rotate(hist_img2, cv2.ROTATE_90_CLOCKWISE)

hist_img1 = cv2.resize(hist_img1, (image.shape[1], image.shape[0]))
hist_img2 = cv2.resize(hist_img2, (image.shape[1], image.shape[0]))


cv2.imshow("image", image)
cv2.imshow("Vertical Projection", hist_img1)
cv2.imshow("Horizontal Projection", hist_img2)
cv2.waitKey(0)
