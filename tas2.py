import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    min_red1 = np.array([0, 100, 100])
    max_red1 = np.array([7, 255, 255])
    min_red2 = np.array([170, 100, 100])
    max_red2 = np.array([180, 255, 255])

    mask_1 = cv2.inRange(hsv, min_red1, max_red1)
    mask_2 = cv2.inRange(hsv, min_red2, max_red2)
    mask = cv2.add(mask_1, mask_2)
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Original', img)
    cv2.imshow('HSV', hsv)
    cv2.imshow('Res', res)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    if not ret:
        print("Кадр не считан")
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
