# Morphological Gradient?
# Gradient means sudden changes
# The Morphological Gradient highlights the boundary (outline) of objects. 

# Original
# ██████████
# ██████████
# ██████████
# ██████████
# After Dilation
# ████████████
# ████████████
# ████████████
# ████████████

# The object becomes larger.

# After Erosion
# ████████
# ████████
# ████████
# ████████

# The object becomes smaller.

# Gradient = Dilation − Erosion
# ████████████
# ██        ██
# ██        ██
# ████████████

# Only the boundary remains.


import cv2
import numpy as np

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Morphological Gradient
gradient = cv2.morphologyEx(
    thresh,
    cv2.MORPH_GRADIENT,
    kernel
)

# Display
cv2.imshow("Threshold", thresh)
cv2.imshow("Morphological Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows() 




# Outer expanded pixels   ✅
# Original boundary       ✅
# Inner boundary          ✅


# "Morphological Gradient gives the object's boundary."

# This is conceptually true, but technically it's more accurate to say:

# Morphological Gradient produces a boundary band whose thickness depends on the kernel size.

# With a 3×3 kernel, the band is thin.

# With a 9×9 kernel, the band becomes much thicker because:

# Dilation expands farther outward.
# Erosion shrinks farther inward.

# So the remaining difference becomes wider.