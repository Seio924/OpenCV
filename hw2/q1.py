import numpy as np, cv2, time
start = time.time()
def print_rects(rects, idx):
    print("-" * 46 + "\n사각형 원소\t\t랜덤 사각형 정보\t\t   넓이\n" + "-" * 46)
    for i in idx:
        print("rects[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" % (i, rects[i][2], rects[i][3], rects[i][0], rects[i][1], rects[i][-1]))
    print()

rands = np.zeros((10000, 5), np.uint16)
idx = np.arange(10000)

starts = cv2.randn(rands[:,:2], 100, 50)
ends = cv2.randn(rands[:,2:-1], 300, 50)
sizes = cv2.absdiff(starts, ends)
areas = sizes[:, 0] * sizes[:, 1]
rects = np.column_stack((rands[:,:2], sizes, areas))

print_rects(rects, idx)
idx = np.argsort(areas)[::-1]
print_rects(rects, idx)

end = time.time()
print(f"{end - start:.5f} sec")