


import numpy as np
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread("cat.jpg")
b, g, r = cv2.split(img)

cv2.imshow("image",img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

# plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()