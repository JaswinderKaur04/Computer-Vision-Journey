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

# Lowe ratio test
good_matches = []

for m, n in matches:

    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

print("Total KNN matches:", len(matches))
print("Good matches:", len(good_matches))