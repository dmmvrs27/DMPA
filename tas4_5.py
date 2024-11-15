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

    moment = cv2.moments(mask)
    area = moment['m00']
    print("Площадь:", area)

    if area > 0:
        width = height = int(np.sqrt(area))
        #Центр объекта
        centr_x = int(moment["m10"] / moment["m00"])
        centr_y = int(moment["m01"] / moment["m00"])

        #Прямоугрльник
        color = (0, 0, 0)
        fat = 3

        cv2.rectangle(img,
            (centr_x - (width // 25), centr_y - (height // 25)),
            (centr_x + (width // 25), centr_y + (height // 25)),
            color, fat)

    cv2.imshow('Traking', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    if not ret:
        print("Кадр не считан")
        break

cap.release()
cv2.destroyAllWindows()