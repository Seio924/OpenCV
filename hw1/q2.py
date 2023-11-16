import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global title, pt, line_thickness

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            start = (pt[0]-(x-pt[0]), pt[1]-(y-pt[1]))
            cv2.rectangle(image, start, (x, y), (255, 0, 0), line_thickness)
            cv2.imshow(title, image)
            pt = (-1, -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            center = ((pt[0] + x)//2, (pt[1] + y)//2)
            dx, dy = center[0] - x, center[1] - y
            radius = int(np.sqrt(dx * dx + dy * dy))
            cv2.circle(image, center, radius, (0, 0, 255), line_thickness)
            cv2.imshow(title, image)
            pt = (-1, -1)

def onChange(value):
    global line_thickness
    line_thickness = value


image = np.full((400, 600, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
line_thickness = 1

title = "Draw Event"
cv2.imshow(title, image)

cv2.createTrackbar("Thickness", title, 1, 10, onChange)
cv2.setMouseCallback(title, onMouse)

cv2.waitKey(0)
