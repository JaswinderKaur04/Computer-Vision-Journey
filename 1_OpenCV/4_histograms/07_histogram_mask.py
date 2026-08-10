import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
img = cv2.imread("cat.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a black mask
mask = np.zeros(gray.shape, np.uint8)

# Create a white rectangle in the center
cv2.rectangle(
    mask,
    (100, 100),
    (400, 400),
    255,
    -1
)

# Calculate histogram only inside the mask
hist = cv2.calcHist(
    [gray],
    [0],
    mask,
    [256],
    [0, 256]
)

# Display original image and mask
cv2.imshow("Original", gray)
cv2.imshow("Mask", mask)

# Display histogram
plt.plot(hist)
plt.title("Histogram of Selected Region")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()