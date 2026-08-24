import cv2
import matplotlib.pyplot as plt

# Read the main image
img = cv2.imread("original_img.jpg")

# Resize the main image
img = cv2.resize(img, (700, 500))

# Read the template
template = cv2.imread("cropped_img.jpg")

# Get template dimensions
h, w = template.shape[:2]

# Perform template matching
result = cv2.matchTemplate(
    img,
    template,
    cv2.TM_CCOEFF
)

# Find minimum and maximum matching values
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Print the results
print("Minimum value:", min_val)
print("Maximum value:", max_val)
print("Minimum location:", min_loc)
print("Maximum location:", max_loc)

# For TM_CCOEFF:
# Higher score = better match
top_left = max_loc

# Calculate bottom-right corner
right = top_left[0] + w
bottom = top_left[1] + h

bottom_right = (right, bottom)

# Draw rectangle around the best match
cv2.rectangle(
    img,
    top_left,
    bottom_right,
    (0, 255, 0),
    2
)

# Display result
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Template Matching - TM_CCOEFF")
plt.axis("off")
plt.show()