import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype=np.uint8)

# Blue horizontal line
img[50] = (255, 0, 0)

# Green vertical line
img[:, 200] = (0, 255, 0)

# Red square
img[150:250, 150:250] = (0, 0, 255)

cv2.imshow("Practice", img)
cv2.waitKey(0)
cv2.destroyAllWindows()