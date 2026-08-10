# 📊 Histograms — OpenCV

> Understanding and analyzing image intensity and color distributions using Python and OpenCV.

---

## 🧭 Overview

A histogram represents the distribution of pixel intensity values in an image.

In this module, I explored grayscale and color histograms, intensity changes, histogram equalization, contrast stretching, and histogram masking.

---

## 🎯 What I Learned

| Topic | What I Learned |
|---|---|
| Grayscale Histogram | Analyzing the distribution of grayscale pixel intensities |
| Intensity Changes | Understanding how changing intensity values affects a histogram |
| Color Histogram | Analyzing Blue, Green, and Red channels separately |
| Histogram Equalization | Improving image contrast |
| Equalization Experiments | Comparing original and equalized images |
| Contrast Stretching | Expanding a limited intensity range |
| Histogram Masking | Analyzing a selected region of an image |

---

## 🧠 Core Concepts

### 1. Grayscale Histogram

A grayscale histogram shows how frequently each pixel intensity occurs in an image.

For an 8-bit grayscale image:

```text
0   → Black
127 → Gray
255 → White

The histogram represents:

X-axis → Pixel Intensity
Y-axis → Number of Pixels
2. Pixel Intensity

Pixel intensity represents the brightness value of a pixel.

Low Intensity  → Dark Pixel
High Intensity → Bright Pixel

For an 8-bit grayscale image, the intensity range is:

0 ───────────────────── 255
Black                  White
3. Histogram Bins

Bins determine how intensity values are grouped.

hist = cv2.calcHist(
    [gray],
    [0],
    None,
    [256],
    [0, 256]
)

Here:

[256]     → 256 bins
[0, 256]  → Intensity range

Using 256 bins allows the histogram to represent individual intensity values from 0 to 255.

4. Color Histogram

OpenCV stores color images in BGR format.

Channel 0 → Blue
Channel 1 → Green
Channel 2 → Red

Each channel can have its own histogram.

This helps analyze how much Blue, Green, and Red information is present in an image.

5. Histogram Equalization

Histogram equalization improves image contrast by redistributing pixel intensity values.

equalized = cv2.equalizeHist(gray)

Basic process:

Original Image
      ↓
Histogram
      ↓
Equalization
      ↓
Improved Contrast
6. Contrast Stretching

Contrast stretching expands a limited intensity range into a wider range.

Before:

50 ───────────── 180

        ↓

After:

0 ───────────────────── 255

This can improve the visibility of details in an image.

7. Histogram Masking

A mask allows us to calculate a histogram for only a selected region of an image.

Full Image
     ↓
   Mask
     ↓
Selected Region
     ↓
  Histogram

This is useful when we want to analyze a specific area instead of the complete image.

🔧 OpenCV Histogram Function

The main OpenCV function used to calculate histograms is:

cv2.calcHist(
    images,
    channels,
    mask,
    histSize,
    ranges
)

Example:

hist = cv2.calcHist(
    [gray],
    [0],
    None,
    [256],
    [0, 256]
)
Parameter	Meaning
images	Input image
channels	Channel to analyze
mask	Region to analyze
histSize	Number of bins
ranges	Intensity range
📂 Project Structure
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
│
└── README.md
🛠️ Technologies
🐍 Python
👁️ OpenCV
🔢 NumPy
📊 Matplotlib
💡 Key Takeaways

Through this module, I learned how to:

Create and interpret grayscale histograms
Understand pixel intensity
Understand histogram bins and intensity ranges
Create BGR color histograms
Analyze changes in pixel intensity
Improve contrast using histogram equalization
Perform contrast stretching
Calculate histograms for selected image regions using masks
