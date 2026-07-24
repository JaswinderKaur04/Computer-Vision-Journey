import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.rectangle(img, (100, 100), (400, 300), (255, 0, 0), 2)

cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -1 means fill the entire space
# cv2.rectangle(img, (100,100), (400,300), (255,0,0), -1)