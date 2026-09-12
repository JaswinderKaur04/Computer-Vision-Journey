import cv2

# Read images
img1 = cv2.imread("images/cat.jpg")
img2 = cv2.imread("images/cat2.jpg")

# Grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ORB
orb = cv2.ORB_create(nfeatures=500)

# Detect descriptors
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# KNN matching
matches = bf.knnMatch(
    des1,
    des2,
    k=2
)

print("Number of KNN matches:", len(matches))

# Display first few matches
for pair in matches[:5]:

    match1, match2 = pair

    print(
        "Best distance:",
        match1.distance,
        "Second best distance:",
        match2.distance
    )