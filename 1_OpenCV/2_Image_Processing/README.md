# 🖼️ Image Processing — OpenCV

> A practical exploration of fundamental image processing techniques using Python and OpenCV.

---

## 🎯 Overview

Image processing is an important foundation of Computer Vision.

In this module, I explored thresholding, image blurring, noise reduction, edge detection, and contour detection.

---

## 🔎 Topics Covered

- **Binary Thresholding** — Convert a grayscale image into a binary image
- **Binary Threshold Experiments** — Understand the effect of different threshold values
- **Binary Inverse Thresholding** — Invert the result of binary thresholding
- **Truncation Thresholding** — Limit pixel intensity values
- **Gaussian Blur** — Smooth images and reduce noise
- **Blur Before Thresholding** — Understand why preprocessing can improve thresholding
- **Median Blur** — Remove noise while preserving edges
- **Bilateral Filtering** — Smooth images while preserving important edges
- **Canny Edge Detection** — Detect edges and boundaries
- **Contour Detection** — Detect and analyze object boundaries

---

## 🧠 Key Concepts

### 1. Binary Thresholding

Binary thresholding converts a grayscale image into a binary image.

```text
Pixel < Threshold  → 0   (Black)
Pixel ≥ Threshold  → 255 (White)
```

Example:

```python
_, thresh = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)
```

---

### 2. Binary Inverse Thresholding

Binary inverse thresholding produces the opposite result of normal binary thresholding.

```text
Pixel < Threshold  → 255 (White)
Pixel ≥ Threshold  → 0   (Black)
```

Example:

```python
_, thresh_inv = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY_INV
)
```

---

### 3. Truncation Thresholding

Truncation limits pixel values above a specified threshold.

```python
_, trunc = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_TRUNC
)
```

Pixels above the threshold are set to the threshold value.

---

## 🌫️ Image Blurring

Blurring is used to reduce noise and smooth an image.

It is often useful before performing operations such as thresholding and edge detection.

---

### 4. Gaussian Blur

Gaussian Blur smooths an image using a Gaussian kernel.

```python
blur = cv2.GaussianBlur(
    img,
    (5, 5),
    0
)
```

Useful for:

- Noise reduction
- Image smoothing
- Preprocessing before edge detection

---

### 5. Blur Before Thresholding

Applying blur before thresholding can reduce unwanted noise and produce a cleaner binary image.

```text
Original Image
      ↓
Gaussian Blur
      ↓
Thresholding
      ↓
Cleaner Binary Image
```

---

### 6. Median Blur

Median Blur replaces each pixel with the median value of its neighborhood.

```python
median = cv2.medianBlur(
    img,
    5
)
```

It is particularly effective for removing salt-and-pepper noise.

---

### 7. Bilateral Filter

Bilateral filtering smooths an image while preserving important edges.

```python
bilateral = cv2.bilateralFilter(
    img,
    9,
    75,
    75
)
```

Unlike simple blurring, bilateral filtering considers both:

- Spatial distance
- Pixel intensity difference

---

## 📐 Canny Edge Detection

Canny Edge Detection is used to identify strong changes in pixel intensity.

```python
edges = cv2.Canny(
    gray,
    100,
    200
)
```

Basic process:

```text
Image
  ↓
Grayscale
  ↓
Noise Reduction
  ↓
Gradient Detection
  ↓
Edge Detection
  ↓
Edge Image
```

Canny is useful for detecting object boundaries and structural features.

---

## 🔍 Contour Detection

Contours represent the boundaries or outlines of objects.

```python
contours, hierarchy = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

Contours can be visualized using:

```python
cv2.drawContours(
    img,
    contours,
    -1,
    (0, 255, 0),
    2
)
```

Contours are useful for:

- Object detection
- Shape analysis
- Boundary detection
- Object measurement

---

## 🔄 Image Processing Pipeline

The techniques explored in this module can be combined into a basic Computer Vision pipeline:

```text
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
```

---

## 📂 Project Structure

```text
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
│
├── cat.jpg
├── practice.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy

---

## 💡 Key Takeaways

Through this module, I learned how to:

- Work with pixel intensity values
- Apply different thresholding techniques
- Convert grayscale images into binary images
- Reduce image noise using different filters
- Compare Gaussian, Median, and Bilateral filtering
- Understand the importance of preprocessing
- Detect edges using Canny
- Detect and visualize object contours
- Build a basic image processing pipeline

---

## 🚀 Next Topic

**Morphological Operations**

> Learning how erosion, dilation, opening, closing, and morphological gradients can be used to refine image structures and remove unwanted noise.
