import cv2

title1 = "color2gray"
color2gray = cv2.imread("./img/img_color.jpg", cv2.IMREAD_GRAYSCALE)

if color2gray is None:
    raise Exception("영상 파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 0)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]

cv2.imwrite("./result_img/img_jpg.jpg", color2gray, params_jpg)
cv2.imwrite("./result_img/img_png.png", color2gray, params_png)

cv2.imshow(title1, color2gray)

cv2.waitKey(0)