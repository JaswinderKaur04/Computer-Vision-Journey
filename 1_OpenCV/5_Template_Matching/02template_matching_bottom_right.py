import cv2

original_img = cv2.imread("original_img.jpg")
tempelate = cv2.imread("cropped_img2.jpg")

result = cv2.matchTemplate(
    original_img,
    tempelate,
    cv2.TM_CCOEFF_NORMED
)

a , b , c , d = cv2.minMaxLoc(result)

# print(a,b,c,d)

bottom_right = d
print(bottom_right)
h , w = tempelate.shape[:2]

top_left = (
    bottom_right[0] + w,
    bottom_right[1] + h
)

result_img = cv2.rectangle(
    original_img,
    bottom_right,
    top_left,
    (0,0,255),
    4
)




cv2.imshow("original image",original_img)
# cv2.imshow("result image",result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


