import cv2

# Read images
img1 = cv2.imread("original_img.jpg")
img2 = cv2.imread("multiple_images_in_one_img.jpg")

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

# Sort by distance
matches = sorted(
    matches,
    key=lambda x: x.distance
)

# Print first 10 matches
for match in matches[:10]:
    print(
        "Query:",
        match.queryIdx,  #queryIdx refers to the descriptor from Image 1.
        "Train:",
        match.trainIdx,   #trainIdx refers to the descriptor from Image 2.
        "Distance:",
        match.distance
    )