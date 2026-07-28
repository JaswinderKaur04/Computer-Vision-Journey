# It is useful when you want the opposite mask.

# 2. Object detection using contours

# Contours generally work well when the object you want to detect is white:

# Object → White (255)
# Background → Black (0)

# Pixel > threshold → 0 (black)
# Pixel ≤ threshold → 255 (white)

import cv2

img = cv2.imread("cat.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

_, binary_inverse = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY_INV
)

cv2.imshow("Original", img)
cv2.imshow("Normal Binary", binary)
cv2.imshow("Binary Inverse", binary_inverse)

cv2.waitKey(0)
cv2.destroyAllWindows()


