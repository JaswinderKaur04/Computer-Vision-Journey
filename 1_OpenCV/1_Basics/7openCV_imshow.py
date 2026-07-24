# Grayscale → 1 channel
# Color (BGR) → 3 channels

# import cv2

# img = cv2.imread("cat.jpg")

# cv2.imshow("My Image", img)

# cv2.waitKey(0)          # 0 means wait forever
# cv2.destroyAllWindows()



# 1: Read as Grayscale (1 channel)

# import cv2

# img = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)

# print(img.shape)



# 2: Read as Color (3 channels)

# import cv2

# img = cv2.imread("cat.jpg")

# print(img.shape)


# Add an Alpha Channel (4 channels)

import cv2

img = cv2.imread("cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

print(img.shape)

cv2.imshow("My Image", img)

cv2.waitKey(0)          
cv2.destroyAllWindows()








# Can we make 5 or 6 channels?

# Yes, as a NumPy array, but not as a standard image format.

import numpy as np

img = np.zeros((300, 300, 5), dtype=np.uint8)

print(img.shape)


# This is just a 5-channel array. Functions like cv2.imshow()
# cannot display it because OpenCV expects images with 1, 3, or
# 4 channels for display.