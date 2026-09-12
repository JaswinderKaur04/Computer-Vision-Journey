import cv2
import matplotlib.pyplot as plt

# ==========================================
# 1. Read Images
# ==========================================

img1 = cv2.imread("images/cat.jpg")
img2 = cv2.imread("images/cat2.jpg")

# Check images
if img1 is None or img2 is None:
    raise FileNotFoundError("Could not load one or both images.")

# ==========================================
# 2. Convert to Grayscale
# ==========================================

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ==========================================
# 3. Create ORB Detector
# ==========================================

orb = cv2.ORB_create(
    nfeatures=500
)

# ==========================================
# 4. Detect Keypoints + Descriptors
# ==========================================

kp1, des1 = orb.detectAndCompute(
    gray1,
    None
)

kp2, des2 = orb.detectAndCompute(
    gray2,
    None
)

print("Image 1 keypoints:", len(kp1))
print("Image 2 keypoints:", len(kp2))

print("Image 1 descriptor shape:", des1.shape)
print("Image 2 descriptor shape:", des2.shape)

# ==========================================
# 5. Create BFMatcher
# ==========================================

bf = cv2.BFMatcher(
    cv2.NORM_HAMMING
)

# ==========================================
# 6. KNN Matching
# ==========================================

matches = bf.knnMatch(
    des1,
    des2,
    k=2
)

print("Total KNN matches:", len(matches))

# ==========================================
# 7. Lowe Ratio Test
# ==========================================

good_matches = []

for m, n in matches:

    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

print("Good matches:", len(good_matches))

# ==========================================
# 8. Draw Good Matches
# ==========================================

result = cv2.drawMatches(
    img1,
    kp1,
    img2,
    kp2,
    good_matches,
    None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# ==========================================
# 9. Display Result
# ==========================================

plt.figure(figsize=(16, 8))

plt.imshow(
    cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
)

plt.title("ORB Feature Matching")
plt.axis("off")

plt.show()