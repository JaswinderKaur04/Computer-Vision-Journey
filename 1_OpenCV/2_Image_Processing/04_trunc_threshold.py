# TRUNC means truncate, or cut off values above a limit
import cv2

img = cv2.imread("cat.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, truncated = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_TRUNC
)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Truncated", truncated)

cv2.waitKey(0)
cv2.destroyAllWindows()


# if pixel > 127:
#     pixel = 127

#Original brightness
#        ↓
# 0 ─────────────── 127 ─────────────── 255
#                   ↑
#              CEILING


# Reducing extreme brightness values
# Limiting the influence of highlights
# Preprocessing before other image-processing operations
# Controlling the range of intensity values


# Object segmentation means:

# Separating the object you are interested in from the rest of the image.

# Imagine this image:

# Original image

# ┌─────────────────────┐
# │                     │
# │      🐱            |
# │                     │
# │                     │
# └─────────────────────┘

