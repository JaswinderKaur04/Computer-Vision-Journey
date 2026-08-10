# 🖼️ Image Processing — OpenCV

> Exploring fundamental image processing techniques using Python and OpenCV.

---

## 🧭 Overview

Image processing is an important foundation of Computer Vision.

In this module, I worked with techniques used to preprocess images, reduce noise, detect edges, identify objects, and extract useful information from images.

---

## 🎯 What I Learned

| Topic | What I Learned |
|---|---|
| Thresholding | Converting images into binary representations |
| Binary Threshold | Separating pixels using a threshold value |
| Binary Inverse | Creating the inverse of a binary image |
| Truncation | Limiting pixel intensity values |
| Gaussian Blur | Smoothing images and reducing noise |
| Median Blur | Removing noise while preserving edges |
| Bilateral Filter | Smoothing while preserving important edges |
| Canny Edge Detection | Detecting edges in images |
| Contours | Detecting and analyzing object boundaries |

---

## 🧠 Core Concepts

### 1. Thresholding

Thresholding separates pixels based on their intensity values.

For binary thresholding:

```text
Pixel < Threshold  → 0
Pixel ≥ Threshold  → 255

Example:

_, thresh = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)
2. Binary Inverse Thresholding

Binary inverse thresholding produces the opposite result of normal binary thresholding.

Binary:

Dark   → Black
Bright → White


Binary Inverse:

Dark   → White
Bright → Black
3. Truncation Thresholding

THRESH_TRUNC limits pixel values above the specified threshold.

_, trunc = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_TRUNC
)

Pixels above the threshold are set to the threshold value.

🌫️ Image Filtering

Filtering is used to smooth images and reduce unwanted noise.

Gaussian Blur
blur = cv2.GaussianBlur(
    img,
    (5, 5),
    0
)

Useful for:

Noise reduction
Image smoothing
Preprocessing before edge detection
Median Blur

Median filtering replaces a pixel with the median value of its neighborhood.

median = cv2.medianBlur(
    img,
    5
)

It is particularly useful for reducing salt-and-pepper noise.

Bilateral Filtering

Bilateral filtering smooths an image while preserving important edges.

bilateral = cv2.bilateralFilter(
    img,
    9,
    75,
    75
)

It considers both:

Spatial distance
Intensity difference
📐 Canny Edge Detection

Canny Edge Detection identifies strong changes in pixel intensity.

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
Gradient
  ↓
Edge Detection
  ↓
Edge Image

Canny is useful for detecting object boundaries and structural features.

🔍 Contour Detection

Contours represent the boundaries or outlines of objects.

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
Boundary detection
🔄 Image Processing Pipeline

The techniques in this module can be combined into a typical preprocessing pipeline:

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
├── practice.py
└── README.md
🛠️ Technologies
🐍 Python
👁️ OpenCV
🔢 NumPy
💡 Key Takeaways

Through this module, I learned how to:

Work with pixel intensity values
Apply different thresholding techniques
Create binary and inverse binary images
Reduce image noise using different filters
Compare Gaussian, Median, and Bilateral filtering
Detect edges using Canny
Detect and visualize object contours
Build basic image preprocessing pipelines
