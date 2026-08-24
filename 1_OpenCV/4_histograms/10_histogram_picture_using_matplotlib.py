import numpy as np
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread("cat.jpg")
cv2.imshow("image window",img)

plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()