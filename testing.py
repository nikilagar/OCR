import numpy as np
import cv2
import matplotlib.pyplot as plt #plt.plot(x,y) plt.show()

img = cv2.imread('images/smallPcapital.png')
mser = cv2.MSER_create(1, 10, 20000, 0.05, 0.02, 200, 1.01, 0.003, 5)
cv2.MSER_create()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()

regions = mser.detectRegions(gray, None)
print(regions)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))
# cv2.putText(vis, str('change'), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
# cv2.fillPoly(vis, hulls, (0, 255, 0))


# cv2.imwrite("test.png", vis)
cv2.imshow('img', vis)
cv2.waitKey(0)
cv2.destroyAllWindows()