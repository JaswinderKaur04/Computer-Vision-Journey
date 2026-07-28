# 1. Gaussian Blur
#    → General smoothing

# 2. Median Blur
#    → Salt-and-pepper noise removal

# 3. Bilateral Filter
#    → Smoothing while preserving edges

# (3, 3) as width × height of the kernel
# kernel is a small matrix (grid) that moves across an image and performs an operation on the pixels.
import cv2

# Read image
img = cv2.imread("cat.jpg")

# Apply Gaussian Blur
blur = cv2.GaussianBlur(
    img,
    (15, 15),   #Window or kernel size
    0
)
# smaller sigma means a narrow curve and less blur. Larger sigma means a wider curve and more blur.
# Larger values means stronger blur. When you set it to 0,
# Display images
cv2.imshow("Original", img)
cv2.imshow("Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()