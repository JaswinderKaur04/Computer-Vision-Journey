# 📊 Histograms — OpenCV

> A practical exploration of image histograms using Python, OpenCV, NumPy, and Matplotlib.

---

## 🎯 Overview

A histogram represents the distribution of pixel intensity values in an image.

In this module, I explored grayscale and color histograms, intensity changes, histogram equalization, contrast stretching, and histogram masking.

---

## 🔎 Topics Covered

- **Grayscale Histogram** — Analyze pixel intensity distribution
- **Intensity Changes** — Understand the effect of changing intensity values
- **Color Histogram** — Analyze BGR channels independently
- **Histogram Equalization** — Improve image contrast
- **Equalization** — Compare original and equalized images
- **Contrast Stretching** — Expand a limited intensity range
- **Histogram Masking** — Analyze a specific region of an image

---

## 🧠 Key Concepts

### 1. Pixel Intensity

For an 8-bit grayscale image:

```text
0   → Black
255 → White
```

Pixel intensity represents the brightness value of a pixel.

---

### 2. Grayscale Histogram

A grayscale histogram shows how frequently each intensity value occurs in an image.

```text
X-axis → Pixel Intensity
Y-axis → Number of Pixels
```

Example:

```python
plt.hist(gray.ravel(), 256, [0, 256])
plt.title("Grayscale Histogram")
plt.show()
```

---

### 3. Histogram Bins

Bins determine how intensity values are grouped.

```python
cv2.calcHist([gray], [0], None, [256], [0, 256])
```

Here:

```text
[256]     → 256 bins
[0, 256]  → Intensity range
```

For an 8-bit grayscale image, the actual intensity values are:

```text
0 → 255
```

---

### 4. Color Histogram

OpenCV uses BGR channel order:

```text
Channel 0 → Blue
Channel 1 → Green
Channel 2 → Red
```

Histograms can be calculated separately for each channel.

```python
blue_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
green_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
red_hist = cv2.calcHist([img], [2], None, [256], [0, 256])
```

This helps understand the distribution of each color channel.

---

### 5. Histogram Equalization

Histogram equalization improves image contrast by redistributing pixel intensity values.

```python
equalized = cv2.equalizeHist(gray)
```

Comparison:

```text
Original Image
      ↓
Original Histogram
      ↓
Histogram Equalization
      ↓
Equalized Image
      ↓
Equalized Histogram
```

---

### 6. Contrast Stretching

Contrast stretching expands a limited intensity range into a wider range.

```text
Before:

50 ───────────── 180

        ↓

After:

0 ───────────────────── 255
```

This can make details more visible when an image has low contrast.

---

### 7. Histogram Masking

A mask allows us to calculate a histogram for a selected region of an image.

```text
Full Image
    ↓
   Mask
    ↓
Selected Region
    ↓
 Histogram
```

Example:

```python
hist = cv2.calcHist(
    [gray],
    [0],
    mask,
    [256],
    [0, 256]
)
```

---

## 🔧 OpenCV Histogram Function

The main OpenCV function used to calculate histograms is:

```python
cv2.calcHist(
    images,
    channels,
    mask,
    histSize,
    ranges
)
```

### Parameters

| Parameter | Meaning |
|---|---|
| `images` | Input image |
| `channels` | Channel to analyze |
| `mask` | Region to analyze |
| `histSize` | Number of bins |
| `ranges` | Intensity range |

---

## 📈 Histogram Visualization

Matplotlib can be used to visualize histograms:

```python
plt.plot(hist)
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.title("Histogram")
plt.show()
```

---

## 📂 Project Structure

```text
4_histograms/
│
├── 01_grayscale_histogram.py
├── 02_histogram_intensitychange.py
├── 03_color_histogram.py
├── 04_histogram_equalization.py
├── 05_equalization.py
├── 06_contrast_stretching.py
├── 07_histogram_mask.py
│
├── cat.jpg
├── squirrel_cls.jpg
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib

---

## 💡 Key Takeaways

Through this module, I learned how to:

- Understand pixel intensity
- Create grayscale histograms
- Understand histogram bins and intensity ranges
- Analyze color channels using histograms
- Visualize intensity distributions
- Apply histogram equalization
- Compare original and equalized images
- Perform contrast stretching
- Calculate histograms for selected image regions using masks

---

## 🚀 Next Topic

**Template Matching**

> Learning how to locate a specific template or object inside a larger image using OpenCV.
