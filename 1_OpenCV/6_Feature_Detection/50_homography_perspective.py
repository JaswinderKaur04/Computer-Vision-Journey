import cv2
import numpy as np

# 1. Read the input image
image = cv2.imread("tilted2.jpeg")

if image is None:
    print("Error: Could not load tilted.jpg")
    exit()

# 2. Define the 4 corners of the object
# Order: Top-Left, Top-Right, Bottom-Right, Bottom-Left

src_points = np.float32([
    [227, 5],       # Top-Left
    [760, 252],    # Top-Right
    [921, 1103],     # Bottom-Right
    [238, 1250]      # Bottom-Left
])

# 3. Desired output size
width, height = 700, 900

# 4. Destination points
dst_points = np.float32([
    [0, 0],           
    [width, 0],       
    [width, height],  
    [0, height]       
])

# 5. Calculate perspective transformation matrix
H = cv2.getPerspectiveTransform(src_points, dst_points)

# 6. Apply perspective transformation
warped_img = cv2.warpPerspective(
    image,
    H,
    (width, height)
)

# 7. Display
cv2.imshow("Original Image", image)
cv2.imshow("Warped Image", warped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()