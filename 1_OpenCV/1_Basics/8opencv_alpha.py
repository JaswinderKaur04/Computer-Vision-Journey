# Alpha = 255 → Draw this pixel completely.
# Alpha = 128 → Draw this pixel with 50% opacity.
# Alpha = 0 → Don't draw this pixel at all.



import cv2

img = cv2.imread("cat.jpg")

# Convert BGR (3 channels) to BGRA (4 channels)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# Make the whole image semi-transparent
img[:, :, 3] = 0      # Try 255, 128, or 0

print(img.shape)

cv2.imshow("My Image", img)

# Save the image
cv2.imwrite("output2.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()