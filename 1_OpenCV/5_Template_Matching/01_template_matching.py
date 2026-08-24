import cv2
import matplotlib.pyplot as plt

# Read the main image
img = cv2.imread("original_img.jpg")

# Read the template
template = cv2.imread("cropped_img.jpg")

# Get template dimensions
h, w = template.shape[:2]

# Perform template matching
result = cv2.matchTemplate(
    img,
    template,
    cv2.TM_CCOEFF_NORMED           #Template Matching Correlation Coefficient Normalized
                                   # Higher score = better match.
)

# Find the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Best match location
top_left = max_loc

# Bottom-right corner
# You're simply calculating where the bottom-right corner should be based on the template size.
bottom_right = (
    top_left[0] + w,
    top_left[1] + h
)

# Print the results
print("Minimum value:", min_val)
print("Maximum value:", max_val)
print("Minimum location:", min_loc)
print("Maximum location:", max_loc)

# Draw rectangle around the match
cv2.rectangle(
    img,
    top_left,
    bottom_right,
    (0, 255, 0),
    2
)

# Display result
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Template Matching")
plt.axis("off")
plt.show() 


# Template Matching

# Advantages:
# ✅ Simple
# ✅ No training
# ✅ Easy to implement
# ✅ Gives location
# ✅ Fast in controlled environments

# Disadvantages:
# ❌ Scale sensitive
# ❌ Rotation sensitive
# ❌ Perspective sensitive
# ❌ Lighting sensitive
# ❌ Occlusion sensitive
# ❌ Can be expensive for large searches

