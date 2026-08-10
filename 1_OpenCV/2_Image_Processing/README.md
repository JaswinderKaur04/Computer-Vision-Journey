# 📊 Histograms — OpenCV

> Understanding and analyzing pixel intensity distributions using OpenCV.

---

## 🧭 Overview

A histogram represents the distribution of pixel intensity values in an image.

It helps us understand:

- 💡 Image brightness
- 🎚️ Image contrast
- 🎨 Color distribution
- 🔍 Intensity patterns
- 🎯 Specific regions of an image

---

## 🎯 What I Learned

| Topic | What I Learned |
|---|---|
| Grayscale Histogram | Distribution of grayscale pixel intensities |
| Pixel Intensity | Brightness value of a pixel |
| Histogram Bins | How intensity values are grouped |
| Intensity Range | `0–255` for 8-bit images |
| Color Histogram | BGR channel distributions |
| Histogram Equalization | Improving image contrast |
| Contrast Stretching | Expanding intensity values |
| Histogram Masking | Analyzing a selected image region |

---

## 🧠 Core Concepts

### Grayscale Histogram

For an 8-bit grayscale image:

```text
0   → Black
127 → Gray
255 → White

A histogram represents:

X-axis → Pixel Intensity
Y-axis → Number of Pixels
Histogram Bins
[256]     → Number of bins
[0, 256]  → Intensity range

Using 256 bins allows each intensity value from 0 to 255 to be represented individually.

🎨 Color Histogram

OpenCV uses BGR channel order:

Channel 0 → Blue
Channel 1 → Green
Channel 2 → Red

Each channel can have its own histogram to analyze the distribution of that color.

📈 Histogram Equalization

Histogram equalization redistributes pixel intensities to improve image contrast.

equalized = cv2.equalizeHist(gray)
Low / Limited Contrast
          ↓
Histogram Equalization
          ↓
Improved Contrast
🔄 Contrast Stretching

Contrast stretching expands a limited intensity range.

Before:

50 ───────────── 180

        ↓

After:

0 ───────────────────── 255

This can make image details more visible.

🎭 Histogram Masking

A mask allows us to calculate a histogram for only a selected region of an image.

Full Image
     ↓
   Mask
     ↓
Selected Region
     ↓
  Histogram

This is useful when we want to analyze a specific part of an image.

🔧 OpenCV

The main function used for calculating histograms is:

cv2.calcHist(
    [gray],
    [0],
    None,
    [256],
    [0, 256]
)
Parameter	Purpose
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
├── cat.jpg
└── README.md
🛠️ Technologies
🐍 Python
👁️ OpenCV
🔢 NumPy
📊 Matplotlib
💡 Key Takeaways

Through this module, I learned how to:

Analyze pixel intensity distributions
Create grayscale and color histograms
Understand bins and intensity ranges
Improve contrast using histogram equalization
Perform contrast stretching
Analyze specific image regions using masks
