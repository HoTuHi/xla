import cv2

x = int(input())
image = cv2.imread('sodoku.jpg')
result = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Remove horizontal lines
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x, 1))
remove_horizontal = cv2.morphologyEx(
    thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
cnts = cv2.findContours(
    remove_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(result, [c], -1, (255, 255, 255), 5)

# Remove vertical lines
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, x))
remove_vertical = cv2.morphologyEx(
    thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=1)
cnts = cv2.findContours(
    remove_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(result, [c], -1, (255, 255, 255), 5)

cv2.imshow('thresh', thresh)
cv2.imshow('result', result)
cv2.imwrite('result.png', result)
cv2.waitKey()
