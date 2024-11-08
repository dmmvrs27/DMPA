import cv2 as cv
import cv2

img = cv2.imread('/Users/denismalysev/Desktop/dog.png')

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('HSV', cv2.WINDOW_NORMAL)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Original Image', img)
cv2.imshow('HSV Image', hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

