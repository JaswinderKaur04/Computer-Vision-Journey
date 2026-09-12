import cv2
import matplotlib.pyplot as plt

# Read images
img1 = cv2.imread("images/cat.jpg")
img2 = cv2.imread("images/cat2.jpg")

# Convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ORB
orb = cv2.ORB_create(nfeatures=500)

# Detect features
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# BFMatcher
bf = cv2.BFMatcher(
    cv2.NORM_HAMMING,
    crossCheck=True
)

# Match
matches = bf.match(des1, des2)

# Sort matches
matches = sorted(
    matches,
    key=lambda x: x.distance
)

# Select best 50 matches
good_matches = matches[:50]

# Draw matches
matched_image = cv2.drawMatches(
    img1,
    kp1,
    img2,
    kp2,
    good_matches,
    None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# Display
plt.figure(figsize=(15, 8))
plt.imshow(cv2.cvtColor(matched_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()