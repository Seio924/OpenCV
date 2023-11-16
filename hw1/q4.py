import numpy as np
import cv2

width, height = 600, 400

red, blue, white = (0, 0, 255), (255, 0, 0), (255, 255, 255)
image = np.full((height, width, 3), white, np.uint8)

big_circle_center = (width//2, height//2)
big_circle_radius = (height//4, height//4)
small_circle_center_red = (big_circle_center[0]-big_circle_radius[0]//2, big_circle_center[1])
small_circle_center_blue = (big_circle_center[0]+big_circle_radius[0]//2, big_circle_center[1])
small_circle_radius = (big_circle_radius[0]//2, big_circle_radius[1]//2)

cv2.ellipse(image, big_circle_center, big_circle_radius,  0, 180, 360, red, -1)
cv2.ellipse(image, big_circle_center, big_circle_radius,  0, 0, 180, blue, -1)
cv2.ellipse(image, small_circle_center_red, small_circle_radius,  0, 0, 180, red, -1)
cv2.ellipse(image, small_circle_center_blue, small_circle_radius,  0, 180, 360, blue, -1)

cv2.imshow("image", image)
cv2.waitKey()