# 📊 Histograms — OpenCV

This module covers image histograms and intensity analysis using OpenCV and Python.

A histogram represents the distribution of pixel intensity values in an image. It helps analyze image brightness, contrast, color distribution, and selected regions of an image.

## 🎯 Learning Objectives

- Understand pixel intensity
- Understand grayscale histograms
- Understand histogram bins and intensity ranges
- Analyze image brightness and contrast using histograms
- Create color histograms using BGR channels
- Apply histogram equalization
- Perform contrast stretching
- Calculate histograms for selected image regions using masks

## 🧠 Key Concepts

### 1. Pixel Intensity

For an 8-bit grayscale image, pixel intensity ranges from:

```text
0 → Black
255 → White

Intensity represents the brightness value of a pixel.

2. Grayscale Histogram

A grayscale histogram counts how many pixels have each intensity value.

X-axis → Pixel Intensity
Y-axis → Number of Pixels

A histogram helps identify whether an image is generally dark, bright, or has low/high contrast.

3. Histogram Bins

Bins are groups used to organize intensity values.

For an 8-bit grayscale image:

[256]

creates 256 bins, allowing each intensity value from 0 to 255 to be represented separately.

Using fewer bins, such as 16, groups multiple intensity values together and produces a less detailed histogram.

4. Intensity Range

The full grayscale intensity range is:

[0, 256]

OpenCV treats the upper boundary as exclusive, so the actual intensity values are:

0 → 255

The number of bins and the intensity range are different concepts:

[256]      → Number of bins
[0, 256]   → Intensity range
🎨 Color Histogram

OpenCV stores color images in BGR order:

Channel 0 → Blue
Channel 1 → Green
Channel 2 → Red

Separate histograms can be calculated for each channel.

Example:

blue_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
green_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
red_hist = cv2.calcHist([img], [2], None, [256], [0, 256])

A color histogram helps analyze the distribution of individual color-channel intensities.

🔧 cv2.calcHist()

Basic syntax:

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
Parameters
Parameter	Meaning
images	Image to analyze
channels	Channel to calculate the histogram for
mask	Region to analyze; None means the whole image
histSize	Number of bins
ranges	Intensity range
📈 Histogram Equalization

Histogram equalization improves image contrast by redistributing pixel intensities.

equalized = cv2.equalizeHist(gray)

It is useful when intensity values are concentrated in a limited range.

🔄 Contrast Stretching

Contrast stretching expands a limited intensity range to a wider range, commonly:

Original range → 0–255

For example:

50 → 0
180 → 255

This can improve the visibility of image details.

🎭 Histogram Masking

A mask can be used to calculate a histogram for only a specific region of an image.

hist = cv2.calcHist(
    [gray],
    [0],
    mask,
    [256],
    [0, 256]
)

With:

mask = None

the histogram is calculated for the entire image.

With a binary mask, the histogram can be calculated only for the selected region.

📂 Project Structure
4_Histograms/
│
├── images/
│   └── cat.jpg
│
├── 01_grayscale_histogram.py
├── 02_histogram_bins.py
├── 03_color_histogram.py
├── 04_histogram_equalization.py
├── 05_contrast_stretching.py
├── 06_histogram_mask.py
└── README.md
🛠️ Technologies Used
Python
OpenCV
NumPy
Matplotlib
📚 What I Learned

Through this module, I learned how to:

Analyze pixel intensity distributions
Create and interpret grayscale histograms
Work with histogram bins and intensity ranges
Analyze BGR color channels separately
Improve image contrast using histogram equalization
Stretch intensity values to improve contrast
Analyze selected image regions using masks
```
