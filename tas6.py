import cv2 as cv
import cv2

cap = cv.VideoCapture(0)

cv.namedWindow('Tas6', cv.WINDOW_NORMAL)

BGR = (0, 0, 255)
fat = 2

while True:
    #Чтение кадра из камеры
    ret, frame = cap.read()
    if not ret:
        break

    #Размеры изображения
    height, width, _ = frame.shape

    #Делаем прямоугольники
    rwidth = 50
    rheight = 400
    left_x = width // 2 - rwidth // 2
    left_y = height // 2 - rheight // 2
    right_x = width // 2 + rwidth // 2
    right_y = height // 2 + rheight // 2

    rect_width_2 = 50
    rect_height_2 = 400
    left_x1 = width // 2 - rheight // 2
    left_y1 = height // 2 - rwidth // 2
    right_x1 = width // 2 + rheight // 2
    right_y1 = height // 2 + rwidth // 2

    cv.rectangle(frame, (left_x, left_y), (right_x, right_y), BGR, fat)
    cv.rectangle(frame, (left_x1, left_y1), (right_x1, right_y1), BGR, fat)

    cv.imshow('Tas6', frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()