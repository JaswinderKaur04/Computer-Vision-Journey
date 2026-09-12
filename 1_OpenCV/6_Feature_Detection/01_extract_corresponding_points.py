import cv2

img1 = cv2.imread("original_img.jpg")
img2 = cv2.imread("tilted.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ORB
orb = cv2.ORB_create(nfeatures=500)

kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# KNN matching
matches = bf.knnMatch(des1, des2, k=2)

# Lowe Ratio Test
good_matches = []

for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

print("Good matches:", len(good_matches))


# Extract corresponding points
pts1 = []
pts2 = []

for m in good_matches:

    pts1.append(kp1[m.queryIdx].pt)        #m.queryIdx is the index of the descriptor/keypoint from Image 1.
    pts2.append(kp2[m.trainIdx].pt)


print("Image 1 points:")
print(pts1[:5])

print("\nImage 2 points:")
print(pts2[:5])



# kp1[497]

# means:

# Give me keypoint number 497 from Image 1.

# Then: kp1[497].pt

# gives its coordinate.

# For eg. (590.0, 408.0)