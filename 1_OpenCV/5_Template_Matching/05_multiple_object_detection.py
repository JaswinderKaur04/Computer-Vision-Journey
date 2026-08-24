import cv2
import matplotlib.pyplot as plt

# Read main image
img = cv2.imread("multiple_images_in_one_img.jpg")

# Read template
template = cv2.imread("cropped_image_from_multiple_img.jpg")

# Get template dimensions
h, w = template.shape[:2]

# Perform template matching
result = cv2.matchTemplate(
    img,
    template,
    cv2.TM_CCOEFF_NORMED
)

# Set matching threshold
threshold = 0.90

# 0.70 → more detections, more false positives
# 0.80 → balanced
# 0.90 → stricter
# 0.95 → very strict

# Find all locations above threshold
locations = zip(*((result >= threshold).nonzero()))

# Draw rectangle around every match
for y, x in locations:

    top_left = (x, y)

    bottom_right = (
        x + w,
        y + h
    )

    cv2.rectangle(
        img,
        top_left,
        bottom_right,
        (0, 255, 0),
        2
    )

# Display result
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Multiple Object Detection")
plt.axis("off")
plt.show()















# result

# After:

# result = cv2.matchTemplate(...)

# result is basically a 2D array of matching scores.

# Imagine:

# result

#        x →
#      0     1     2
#    ┌─────┬─────┬─────┐
# y 0│ 0.2 │ 0.9 │ 0.3 │
#    ├─────┼─────┼─────┤
#   1│ 0.8 │ 0.4 │ 0.95│
#    ├─────┼─────┼─────┤
#   2│ 0.1 │ 0.92│ 0.3 │
#    └─────┴─────┴─────┘

# Suppose:

# threshold = 0.90
# 2. result >= threshold
# result >= threshold

# means:

# Check every matching score and ask whether it is ≥ 0.90.

# So:

# 0.2  → False
# 0.9  → True
# 0.3  → False

# 0.8  → False
# 0.4  → False
# 0.95 → True

# 0.1  → False
# 0.92 → True
# 0.3  → False

# Giving:

# False  True   False
# False  False  True
# False  True   False

# So now we know which locations are good matches.

# 3. .nonzero()

# Now:

# (result >= threshold).nonzero()

# means:

# Give me the coordinates where the value is True.

# From:

# False  True   False
# False  False  True
# False  True   False

# the True positions are:

# (y, x)

# (0, 1)
# (1, 2)
# (2, 1)

# Remember:

# y = row
# x = column

# So these are the locations where our template was detected.





# 1. What is zip()?

# Python's zip() is used to combine corresponding elements from two or more sequences.

# Simple example
# names = ["Aman", "Rahul", "Priya"]
# marks = [80, 90, 85]

# result = zip(names, marks)

# print(list(result))

# Output:

# [('Aman', 80), ('Rahul', 90), ('Priya', 85)]

# Why?

# Python pairs them by position:

# names       marks

# Aman   ──── 80
# Rahul  ──── 90
# Priya  ──── 85

# So zip() creates:

# (Aman, 80)
# (Rahul, 90)
# (Priya, 85)


# y = [100, 200, 300]

# x = [50, 150, 250]

# We want to combine them:

# (100, 50)
# (200, 150)
# (300, 250)

# We can do:

# zip(y, x)

# which gives:

# (100, 50)
# (200, 150)
# (300, 250)

# Then:

# for y, x in zip(y, x):

# lets us process each coordinate pair.



# 6. But our code has *

# Here's the confusing part:

# zip(*((result >= threshold).nonzero()))

# Don't try to understand everything at once.

# First imagine:

# (result >= threshold).nonzero()

# returns:

# (
#     [0, 1, 1, 2],    # y
#     [1, 0, 2, 1]     # x
# )

# Without *, we would have:

# zip(
#     ([0, 1, 1, 2],
#      [1, 0, 2, 1])
# )

# But we want to give the two lists to zip() as two separate arguments:

# zip(
#     [0, 1, 1, 2],
#     [1, 0, 2, 1]
# )

# The * does exactly that.

# 7. What does * mean here?

# In this situation, * means:

# Unpack the elements.

# For example:

# values = [
#     [1, 2, 3],
#     [10, 20, 30]
# ]