import cv2

# Read two images
img1 = cv2.imread("original_img.jpg")
img2 = cv2.imread("multiple_images_in_one_img.jpg")

# Convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create ORB
orb = cv2.ORB_create(nfeatures=500)

# Detect keypoints and descriptors
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# Create BFMatcher
bf = cv2.BFMatcher(
    cv2.NORM_HAMMING,
    crossCheck=True
)

# Match descriptors
matches = bf.match(des1, des2)

print("Number of matches:", len(matches))

# Inspect first match
match = matches[0]

print("Query index:", match.queryIdx)
print("Train index:", match.trainIdx)
print("Distance:", match.distance)