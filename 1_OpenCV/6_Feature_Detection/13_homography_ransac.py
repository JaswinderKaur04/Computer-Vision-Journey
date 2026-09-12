import cv2
import numpy as np

# 1. Read images
img1 = cv2.imread("multiple_images_in_one_img.jpg")
img2 = cv2.imread("cropped_image_from_multiple_img.jpg")

if img1 is None or img2 is None:
    raise FileNotFoundError("Could not load one or both images.")

# 2. Convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 3. Detect ORB features
orb = cv2.ORB_create(nfeatures=500)

kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# 4. Feature matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

matches = bf.knnMatch(des1, des2, k=2)

# 5. Lowe Ratio Test
good_matches = []

for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

print("Good matches:", len(good_matches))

# 6. Extract corresponding points
pts1 = []
pts2 = []

for m in good_matches:
    pts1.append(kp1[m.queryIdx].pt)
    pts2.append(kp2[m.trainIdx].pt)

pts1 = np.float32(pts1)
pts2 = np.float32(pts2)

# 7. Calculate Homography using RANSAC
if len(good_matches) >= 4:

    H, mask = cv2.findHomography(
        pts1,
        pts2,
        cv2.RANSAC,
        5.0
    )

    print("\nHomography Matrix:")
    print(H)

    print("\nRANSAC Mask:")
    print(mask.ravel())

    # 8. Count inliers and outliers
    inliers = np.sum(mask)
    outliers = len(mask) - inliers

    print("\nInliers:", inliers)
    print("Outliers:", outliers)

else:
    print("Not enough good matches for Homography.")