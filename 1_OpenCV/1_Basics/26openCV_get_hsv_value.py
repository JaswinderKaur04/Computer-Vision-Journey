# H = Hue (the actual color)
# S = Saturation (how pure the color is)
# V = Value (brightness)
import cv2

current_frame = None

def mouse(event, x, y, flags, param):
    global current_frame

    if event == cv2.EVENT_LBUTTONDOWN:
        hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        h, s, v = hsv[y, x]

        print("HSV =", h, s, v)

cap = cv2.VideoCapture(0)

cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", mouse)

while True:
    ret, frame = cap.read()

    current_frame = frame.copy()

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




# Every color has an angle on this wheel.

# 🔴 Red = 0°
# 🟡 Yellow = 60°
# 🟢 Green = 120°
# 🔵 Blue = 240°

# Now look at your BGR value:

# B = 0
# G = 255
# R = 255

# This means:

# No blue
# Full green
# Full red

# When you mix Red + Green, you get Yellow.

# Since yellow is located at 60° on the color wheel, its Hue = 60° (in the standard HSV system).

# Why does OpenCV print 30 instead of 60?

# OpenCV stores Hue in the range 0 to 179, not 0 to 360.

# So it simply scales the angle by dividing it by 2:

# Standard Hue = 60°
#           ↓
# OpenCV stores = 60 ÷ 2 = 30

# -------------------------------------------------------------------

# B = 10
# G = 255   ← Maximum
# R = 150

# Since Green is the maximum, the standard HSV formula is:

# Hue = 60 × (2 + (B - R) / (Max - Min))

# Substitute the values:

# Hue = 60 × (2 + (10 - 150) / (255 - 10))
#      = 60 × (2 - 140 / 245)
#      = 60 × (2 - 0.5714)
#      = 60 × 1.4286
#      ≈ 85.7°

# This is the standard HSV hue.
# ----------------------------------------------------------------------
# V = max(B, G, R)
# ----------------------------------------------------------------------
# S = (Max - Min) / Max × 255