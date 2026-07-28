# Edge Detection with Canny
# An edge is a place where there is a strong change in brightness or color


import cv2

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(
    gray,
    50,
    400
)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 100 → Lower threshold
# 200 → Upper threshold
# Brightness change
#        │
#        ▼
# 0 ─────────── 100 ─────────── 200 ─────────── 255
#        │             │              │
#        │             │              │
#     No edge       Weak edge      Strong edge