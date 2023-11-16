import numpy as np
import cv2

mat1 = np.full((200, 300), 100, np.uint8)
mat2 = np.full((200, 300), 100, np.uint8)

mat1_title, mat2_title = 'win mode1', 'win mode2'

cv2.imshow(mat1_title, mat1)
cv2.imshow(mat2_title, mat2)

cv2.moveWindow(mat1_title, 0, 0)
cv2.moveWindow(mat2_title, 300, 200)

cv2.waitKey(0)
cv2.destroyAllWindows()