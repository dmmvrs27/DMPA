import cv2 as cv
import cv2

#Задание 3 Отобразить видео в окне. Рассмотреть методы класса
#VideoCapture и попробовать отображать видео в разных форматах, в частности
#размеры и цветовая гамма.

cap = cv2.VideoCapture('/Users/denismalysev/Desktop/dog.mp4')
cv2.namedWindow('Video1', cv2.WINDOW_NORMAL)
cv2.namedWindow('Video2', cv2.WINDOW_NORMAL)
cv2.namedWindow('Video3', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Video1', 800, 600)
cv2.resizeWindow('Video2', 1024, 1000)
cv2.resizeWindow('Video3', 1800, 800)

# чтение видеофайла кадр за кадром
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

        cv2.imshow('Video1', gray)
        cv2.imshow('Video2', hsv)
        cv2.imshow('Video3', lab)

        if cv2.waitKey(25) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()