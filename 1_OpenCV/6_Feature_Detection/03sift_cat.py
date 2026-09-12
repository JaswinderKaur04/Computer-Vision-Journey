import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("original_img.jpg", cv2.IMREAD_GRAYSCALE)

# Create two Gaussian-blurred images
blur1 = cv2.GaussianBlur(img, (5, 5), 1)
blur2 = cv2.GaussianBlur(img, (5, 5), 2)

# Difference of Gaussian
dog = blur1.astype("float32") - blur2.astype("float32")

# Convert DoG to displayable image
dog = cv2.normalize(
    dog,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

dog = dog.astype("uint8")

# Display
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(blur1, cmap="gray")
plt.title("Gaussian Blur 1")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(dog, cmap="gray")
plt.title("Difference of Gaussian")
plt.axis("off")

plt.show()