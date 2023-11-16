import numpy as np, cv2

logo = cv2.imread("img/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상 파일 읽기 오류 ")

b, g, r = cv2.split(logo)
zeros = np.zeros((logo.shape[0], logo.shape[1]), dtype="uint8")

blue_img = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img = cv2.merge([zeros, zeros, r])

cv2.imshow("logo", logo)
cv2.imshow("red_img", red_img)
cv2.imshow("green_img", green_img)
cv2.imshow("blue_img", blue_img)
cv2.waitKey()