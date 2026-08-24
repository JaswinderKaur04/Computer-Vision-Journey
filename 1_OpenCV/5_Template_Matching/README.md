
# #Template Matching

Template Matching is an OpenCV technique used to find a small image (template) inside a larger image.

It works by sliding the template over the main image and calculating a matching score at different locations.

## #Topics Covered

- Template Cropping
- Basic Template Matching
- Template Dimensions
- Matching Score
- Best Match Detection
- `cv2.minMaxLoc()`
- Bounding Box
- Top-Left and Bottom-Right Coordinates
- Multiple Object Detection
- Matching Threshold
- `nonzero()`
- `zip()`

## 1. Template Cropping

A small part of the original image is cropped and used as the template.

The template is then searched inside the larger/main image.

## 2. Template Dimensions

The height and width of the template are obtained using:

    h, w = template.shape[:2]

Here:

    h → Template height
    w → Template width

These dimensions are important when creating the bounding box around the detected object.

## 3. Template Matching

OpenCV provides `cv2.matchTemplate()` to compare the template with different regions of the main image.

    result = cv2.matchTemplate(
        img,
        template,
        cv2.TM_CCOEFF_NORMED
    )

`TM_CCOEFF_NORMED` produces normalized matching scores.

A score closer to `1` generally indicates a stronger match.

## 4. Finding the Best Match

The best match can be found using:

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

The returned values are:

    min_val  → Minimum matching score
    max_val  → Maximum matching score
    min_loc  → Location of minimum score
    max_loc  → Location of maximum score

For `TM_CCOEFF_NORMED`, `max_loc` is used because the highest score represents the best match.

## 5. Top-Left Coordinate

The location of the best match is stored in:

    top_left = max_loc

For example:

    top_left = (100, 200)

This means:

    x = 100
    y = 200

This point represents the top-left corner of the detected template.

## 6. Bottom-Right Coordinate

The bottom-right corner is calculated using the template's width and height.

    bottom_right = (
        top_left[0] + w,
        top_left[1] + h
    )

For example:

    top_left = (100, 200)
    w = 150
    h = 100

Then:

    bottom_right = (250, 300)

The template dimensions are used here, not the dimensions of the original image.

## 7. Drawing the Bounding Box

The detected object can be surrounded by a rectangle using:

    cv2.rectangle(
        img,
        top_left,
        bottom_right,
        (0, 255, 0),
        2
    )

The rectangle is defined using two points:

    Top-left
        ↓
    (x, y)

    Bottom-right
        ↓
    (x + width, y + height)

## 8. Multiple Object Detection

Basic Template Matching finds the best match.

To detect multiple occurrences of the same template, a threshold can be used.

    threshold = 0.90

All matching locations whose score is greater than or equal to the threshold are selected.

    locations = zip(*((result >= threshold).nonzero()))

Then every detected location is processed:

    for y, x in locations:

        top_left = (x, y)

        bottom_right = (
            x + w,
            y + h
        )

        cv2.rectangle(
            img,
            top_left,
            bottom_right,
            (0, 255, 0),
            2
        )

## 9. Matching Threshold

The threshold controls how strict the detection is.

    0.70 → More detections, more false positives
    0.80 → Moderate
    0.90 → Stricter
    0.95 → Very strict

A higher threshold means the detected region must have a stronger similarity to the template.

## 10. Understanding `nonzero()`

The following code finds the coordinates where the matching score is greater than or equal to the threshold.

    (result >= threshold).nonzero()

First:

    result >= threshold

checks every matching score.

For example:

    0.20  0.95  0.30
    0.91  0.40  0.97
    0.10  0.92  0.30

With:

    threshold = 0.90

the result becomes conceptually:

    False  True  False
    True   False True
    False  True  False

`nonzero()` finds the coordinates of the `True` values.

These coordinates represent possible template matches.

## 11. Understanding `zip()`

`zip()` combines corresponding elements from sequences.

Example:

    y = [100, 200, 300]
    x = [50, 150, 250]

Using:

    zip(y, x)

produces coordinate pairs:

    (100, 50)
    (200, 150)
    (300, 250)

In multiple-object Template Matching:

    locations = zip(*((result >= threshold).nonzero()))

The `*` unpacks the arrays returned by `nonzero()` so that `zip()` can pair the corresponding `y` and `x` coordinates.

Then:

    for y, x in locations:

processes each detected location one by one.

## 12. Complete Template Matching Flow

    Main Image
         +
      Template
         ↓
    cv2.matchTemplate()
         ↓
    Matching Scores
         ↓
    Find Best Match
         ↓
    Get Match Location
         ↓
    Calculate Top-Left
         ↓
    Calculate Bottom-Right
         ↓
    Draw Bounding Box

For multiple objects:

    Main Image
         +
      Template
         ↓
    cv2.matchTemplate()
         ↓
    Matching Scores
         ↓
    Apply Threshold
         ↓
    Find All Matching Locations
         ↓
    Calculate Bounding Boxes
         ↓
    Detect Multiple Objects

## 13. Advantages

- Simple to understand
- Easy to implement
- No training required
- No machine learning model required
- Fast in controlled environments
- Provides the location of the matching object
- Useful when the object's appearance remains consistent
- Useful for simple automation and inspection tasks
- Can detect multiple occurrences using thresholding

## 14. Disadvantages

- Scale sensitive
- Rotation sensitive
- Perspective sensitive
- Lighting sensitive
- Occlusion sensitive
- Can produce false positives
- Large search areas can be computationally expensive
- Requires a suitable template
- Does not actually understand the object
- Multiple detections can produce overlapping bounding boxes

## 15. Important Limitation — Scale

Template Matching is sensitive to the size of the template.

If the template and the object in the main image have different sizes, the matching result can be incorrect.

For example:

    Template size
         ↓
      Small cup

    Main image
         ↓
      Large cup

The algorithm may detect only a part of the object or fail to find the correct match.

This is one of the important disadvantages of Template Matching.

## 16. Important Limitation — Rotation

If the object in the main image is rotated but the template is not rotated, the matching score can decrease.

    Template
       ↓
      Cup

    Main Image
       ↓
      Rotated Cup

The result may not be accurate.

## 17. Important Limitation — Perspective

If the object is viewed from a different angle, its appearance changes.

Template Matching may fail when there is a significant perspective change.

## 18. Important Limitation — Lighting

Changes in brightness, shadows, or illumination can affect the matching score.

Therefore, Template Matching works best when the lighting conditions are relatively controlled.

## 19. Important Limitation — Occlusion

If part of the object is hidden, the template may no longer match correctly.

For example:

    Complete object
        ↓
      Detected

    Partially hidden object
        ↓
      May not be detected

## 20. Practical Work Completed

The following practical concepts were implemented:

- Cropping an image to create a template
- Basic Template Matching
- Finding the best matching location
- Getting template height and width
- Understanding `cv2.minMaxLoc()`
- Calculating `top_left`
- Calculating `bottom_right`
- Drawing bounding boxes
- Detecting multiple objects
- Applying matching thresholds
- Understanding `nonzero()`
- Understanding `zip()`

## 21. Important OpenCV Functions

    cv2.imread()
    cv2.resize()
    cv2.matchTemplate()
    cv2.minMaxLoc()
    cv2.rectangle()
    cv2.cvtColor()

## 22. Important Python / NumPy Concepts

    template.shape
    nonzero()
    zip()

## 23. Key Takeaways

Template Matching follows the basic process:

    Template
        ↓
    Compare with Main Image
        ↓
    Calculate Matching Scores
        ↓
    Find Best / Acceptable Matches
        ↓
    Get Coordinates
        ↓
    Calculate Bounding Box
        ↓
    Detect Object

The most important concepts learned are:

    1. Template
    2. Matching Score
    3. Threshold
    4. Match Location
    5. Template Width and Height
    6. Top-Left Coordinate
    7. Bottom-Right Coordinate
    8. Bounding Box
    9. Multiple Object Detection
    10. False Positives
    11. Scale Sensitivity
    12. Rotation Sensitivity
    13. Perspective Sensitivity
    14. Lighting Sensitivity
    15. Occlusion Sensitivity

## Next Topic

The next topic in the Computer Vision journey is:

ORB — Oriented FAST and Rotated BRIEF

Topics:

- ORB Keypoint Detection
- ORB Descriptors
- Feature Matching
- Hamming Distance
- BFMatcher
- Feature Matching Visualization
- Feature-based Object Recognition
