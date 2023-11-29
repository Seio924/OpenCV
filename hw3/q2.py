import numpy as np, cv2, time

image = cv2.imread("img/test.jpg", cv2.IMREAD_COLOR)
start = time.time()

R, G, B = cv2.split(image)
Y = np.clip(0.299 * R + 0.587 * G + 0.114 * B, 0, 255)
Cb = np.clip((B - Y) * 0.564 + 128, 0, 255)
Cr = np.clip((R - Y) * 0.713 + 128, 0, 255)
YCbCr = cv2.merge([Y, Cb, Cr])

Y, Cb, Cr = cv2.split(YCbCr)
R = np.clip(Y + 1.403 * (Cr - 128), 0, 255)
G = np.clip(Y - 0.714 * (Cr - 128) - 0.344 * (Cb - 128), 0, 255)
B = np.clip(Y + 1.773 * (Cb - 128), 0, 255)
image_revised = cv2.merge([R, G, B])

end = time.time()
print(f"{end - start:.5f} sec")

cv2.imshow("original", image)
cv2.imshow("YCbCr", cv2.convertScaleAbs(YCbCr))
cv2.imshow("revised", cv2.convertScaleAbs(image_revised))
cv2.waitKey(0)
cv2.destroyAllWindows()