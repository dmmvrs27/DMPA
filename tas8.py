import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('Tas8', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2
    centrlnypix = frame[center_y, center_x]

    blue, green, red = centrlnypix
    if red > green and red > blue:
        color = (0, 0, 255)
    elif green > red and green > blue:
        color = (0, 255, 0)
    elif blue > red and blue > green:
        color = (255, 0, 0)
    else:
        color = (0, 0, 0)

    #Делаем прямоугольники
    rwidth = 50
    rheight = 400
    left_x = width // 2 - rwidth // 2
    left_y = height // 2 - rheight // 2
    right_x = width // 2 + rwidth // 2
    right_y = height // 2 + rheight // 2

    rect_width_2 = 50
    rect_height_2 = 400
    left_x1 = width // 2 - rect_height_2 // 2
    left_y1 = height // 2 - rwidth // 2
    right_x1 = width // 2 + rect_height_2 // 2
    right_y1 = height // 2 + rwidth // 2

    cv2.rectangle(frame, (left_x, left_y), (right_x, right_y), color, -1)
    cv2.rectangle(frame, (left_x1, left_y1), (right_x1, right_y1), color, -1)

    cv2.imshow('Tas8', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
