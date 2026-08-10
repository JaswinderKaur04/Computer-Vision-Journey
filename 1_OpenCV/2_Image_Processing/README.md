
# 🖼️ Image Processing — OpenCV

This module covers fundamental image processing techniques using Python and OpenCV.

The goal of this module is to understand how images can be transformed, enhanced, filtered, thresholded, and analyzed before applying advanced Computer Vision techniques.

---

## 🎯 Learning Objectives

- Understand image representation and pixel values
- Perform image thresholding
- Work with binary and inverse binary images
- Apply different thresholding techniques
- Understand image smoothing and blurring
- Reduce image noise
- Detect edges using Canny Edge Detection
- Detect object boundaries using contours
- Understand the importance of preprocessing in Computer Vision

---

## 🧠 Topics Covered

### 1. Binary Thresholding

Binary thresholding converts a grayscale image into a binary image.

Pixels are classified into two values:

```text
Below threshold → 0   (Black)
Above threshold → 255 (White)

Example:

_, thresh = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)
2. Binary Threshold Experiment

Experimented with different threshold values to understand how changing the threshold affects the resulting image.

Low threshold  → More white pixels
High threshold → More black pixels
3. Binary Inverse Thresholding

Binary inverse thresholding produces the opposite result of normal binary thresholding.

_, thresh_inv = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY_INV
)
Normal Binary:
Dark  → Black
Bright → White

Binary Inverse:
Dark  → White
Bright → Black
4. Truncation Thresholding

THRESH_TRUNC limits pixel intensities above the specified threshold.

_, trunc = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_TRUNC
)

Pixels above the threshold are set to the threshold value.

Original:
0 ─────────────── 127 ─────────────── 255

After TRUNC:
0 ─────────────── 127
                  ↑
          maximum value
🌫️ Image Blurring and Filtering

Blurring is used to reduce noise and smooth an image.

It is also useful as a preprocessing step before edge detection and thresholding.

5. Gaussian Blur

Gaussian Blur smooths an image using a Gaussian kernel.

blur = cv2.GaussianBlur(
    img,
    (5, 5),
    0
)

Applications:

Noise reduction
Image smoothing
Preprocessing before edge detection
6. Blur Before Thresholding

Blurring an image before thresholding can reduce small noise and produce a cleaner binary image.

Typical pipeline:

Original Image
      ↓
Grayscale
      ↓
Gaussian Blur
      ↓
Thresholding
      ↓
Binary Image
7. Median Blur

Median Blur replaces each pixel with the median value of its neighborhood.

median = cv2.medianBlur(
    img,
    5
)

It is particularly useful for reducing salt-and-pepper noise while preserving edges better than some simple averaging methods.

8. Bilateral Filtering

Bilateral filtering smooths an image while preserving important edges.

bilateral = cv2.bilateralFilter(
    img,
    9,
    75,
    75
)

Unlike ordinary blurring, bilateral filtering considers both:

Spatial distance
Intensity difference

This allows it to reduce noise while maintaining edges.

📐 Edge Detection
9. Canny Edge Detection

Canny Edge Detection identifies strong intensity changes in an image.

edges = cv2.Canny(
    gray,
    100,
    200
)

Basic pipeline:

Image
  ↓
Grayscale
  ↓
Noise Reduction
  ↓
Gradient Calculation
  ↓
Edge Detection
  ↓
Edge Image

Canny is useful for detecting object boundaries and structural features.

🔍 Contour Detection
10. Contours

A contour represents the boundary or outline of an object.

Contours can be detected using:

contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

Contours can then be drawn using:

cv2.drawContours(
    img,
    contours,
    -1,
    (0, 255, 0),
    2
)

Contours are useful for:

Object detection
Shape analysis
Object measurement
Finding object boundaries
🔄 Image Processing Pipeline

The concepts in this module can be combined into a typical Computer Vision preprocessing pipeline:

Input Image
     ↓
Grayscale Conversion
     ↓
Noise Reduction
     ↓
Thresholding
     ↓
Edge Detection
     ↓
Contour Detection
     ↓
Object / Shape Analysis
📂 Project Structure
2_Image_Processing/
│
├── 01_binary_threshold.py
├── 02_binary_threshold_experiment.py
├── 03_binary_inverse_threshold.py
├── 04_trunc_threshold.py
├── 05image_GaussianBlur.py
├── 06_blur_before_threshold.py
├── 07_median_blur.py
├── 08_bilateral_filter.py
├── 09_canny_edge_detection.py
├── 10_contours.py
├── README.md
└── practice.py
🛠️ Technologies Used
Python
OpenCV
NumPy
📚 What I Learned

Through this module, I learned how to:

Understand pixel intensity values
Convert images into binary representations
Apply different thresholding techniques
Understand the effect of threshold values
Reduce image noise using different filters
Compare Gaussian, Median, and Bilateral filtering
Detect edges using Canny Edge Detection
Detect and visualize object contours
Build basic image preprocessing pipelines
