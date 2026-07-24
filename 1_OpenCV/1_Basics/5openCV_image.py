import cv2

img = cv2.imread("cat.jpg")

print(img)


print(img.ndim)

print("Data Type :", img.dtype)

print("Shape :", img.shape)

# uint8 is one of the most important data types in image processing.

# uint8 stands for:
# u → Unsigned (no negative numbers)
# int → Integer
# 8 → 8 bits (1 byte) of memory

# Since 8 bits can represent 2**8=256 different values.
# A uint8 number can store values from:0 to 255

 