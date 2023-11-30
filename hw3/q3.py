import numpy as np, cv2

# 이미지 파일을 읽기 (BGR 포맷)
img = cv2.imread('img/image3.jpg', cv2.IMREAD_COLOR)

# BGR에서 HSV로 변환
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 계급 개수 설정
h_bins = 30
s_bins = 48

result_size = (h_bins * 10, s_bins * 10, 3)  # 크기 조정

# 2차원 히스토그램 계산
hist_2d = cv2.calcHist([hsv_img], [0, 1], None, [h_bins, s_bins], [0, 180, 0, 256])

# 최대 빈도 값 구하기
max_frequency = np.max(hist_2d)

# 정규화된 히스토그램을 0~1로 스케일 조정
hist_2d_normalized = hist_2d / max_frequency

# HSV 이미지 생성
hsv_color_img = np.zeros((h_bins, s_bins, 3), dtype=np.uint8)

# 히스토그램 값을 HSV 이미지에 복사
for i in range(h_bins):
    for j in range(s_bins):
        h_value = int(i * 180 / h_bins)  # 계급 개수에 따라 정규화
        s_value = int(j * 256 / s_bins)  # 계급 개수에 따라 정규화
        v_value = int(hist_2d_normalized[i, j] * 255)  # 빈도수에 따라 정규화

        hsv_color_img[i, j, :] = [h_value, s_value, v_value]

# HSV 이미지를 BGR로 변환
result_img = cv2.cvtColor(hsv_color_img, cv2.COLOR_HSV2BGR)

result_img2 = np.full(result_size, 0, dtype=np.uint8)

for i in range(h_bins):
    for j in range(s_bins):
        result_img2[i * 10: (i + 1) * 10, j * 10: (j + 1) * 10] = result_img[i, j]


# 히스토그램을 이미지로 출력
cv2.imshow('HSV Color Histogram', result_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()