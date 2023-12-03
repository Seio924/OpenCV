import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("img/filter_sharpen.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

R, G, B = cv2.split(image)

mask_blur = np.array([1/25, 1/25, 1/25,1/25, 1/25,
    1/25, 1/25, 1/25,1/25, 1/25,
    1/25, 1/25, 1/25,1/25, 1/25,
    1/25, 1/25, 1/25,1/25, 1/25,
    1/25, 1/25, 1/25,1/25, 1/25 ], np.float32).reshape(5, 5)

mask_sharpen = np.array([
    0, 0, -1, 0, 0,
    0, -1, -1, -1, 0,
    -1, -1, 13, -1, -1,
    0, -1, -1, -1, 0,
    0, 0, -1, 0, 0
], np.float32).reshape(5, 5)

avg_blur_R = filter(R, mask_blur)
avg_blur_G = filter(G, mask_blur)
avg_blur_B = filter(B, mask_blur)

sharpen_R = filter(R, mask_sharpen)
sharpen_G = filter(G, mask_sharpen)
sharpen_B = filter(B, mask_sharpen)

bluring_User = cv2.merge([avg_blur_R, avg_blur_G, avg_blur_B])
bluring_User = cv2.convertScaleAbs(bluring_User)
sharpen_User = cv2.merge([sharpen_R, sharpen_G, sharpen_B])
sharpen_User = cv2.convertScaleAbs(sharpen_User)

bluring_OpenCV = cv2.convertScaleAbs(cv2.filter2D(image, cv2.CV_16S, mask_blur))
sharpen_OpenCV = cv2.convertScaleAbs(cv2.filter2D(image, cv2.CV_16S, mask_sharpen))

titles = ['image', 'bluring User', 'bluring OpenCV', 'sharpen User', 'sharpen OpenCV']

cv2.imshow('image', image)
cv2.imshow('bluring User', bluring_User)
cv2.imshow('bluring OpenCV', bluring_OpenCV)
cv2.imshow('sharpen User', sharpen_User)
cv2.imshow('sharpen OpenCV', sharpen_OpenCV)
cv2.waitKey(0)