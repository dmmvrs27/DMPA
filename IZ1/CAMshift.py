import cv2
import numpy as np
import time

#Функция для обновления гистограммы
def updateHistograms(imgBGR, curWindow):
    bgrObjectRoi = imgBGR[curWindow[1]: curWindow[1] + curWindow[3],
                          curWindow[0]: curWindow[0] + curWindow[2]]
    hsvObjectRoi = cv2.cvtColor(bgrObjectRoi, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvObjectRoi,
                       np.array((0., 50., 50.)),
                       np.array((180., 255., 255.)))

    histObjectRoi = cv2.calcHist([hsvObjectRoi], [0], mask, [180], [0, 180])
    return cv2.normalize(histObjectRoi, histObjectRoi, 0, 255, cv2.NORM_MINMAX)


#Открытие видеофайла
video = cv2.VideoCapture("video1.mp4")

if not video.isOpened():
    print("Не удалось открыть видео. Проверьте путь к файлу.")
    exit()

#Чтение первого кадра
ok, frame = video.read()

if not ok:
    print("Не удалось прочитать первый кадр видео.")
    exit()

#Выбор ROI (области для отслеживания)
bbox = cv2.selectROI("Tracking", frame, False)
cv2.destroyWindow("Tracking")

#Настройка критерий для CamShift
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

#Инициализация
currentWindow = bbox
histObjectRoi = updateHistograms(frame, currentWindow)

frame_count = 0  #Количество обработанных кадров
lost_frame_count = 0  #Количество кадров, на которых трекер потерял объект
start_time = time.time()  #Время начала процесса

while True:
    ok, frame = video.read()
    if not ok:
        break

    timer = cv2.getTickCount()
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Обратная проекция
    backProjectedImg = cv2.calcBackProject([imgHSV], [0], histObjectRoi, [0, 180], 1)

    #Применение CamShift
    rotatedWindow, curWindow = cv2.CamShift(backProjectedImg, currentWindow, term_criteria)

    #Обновление текущего окна
    if curWindow[2] > 0 and curWindow[3] > 0:
        currentWindow = curWindow
    else:
        lost_frame_count += 1

    #Рисование рамки отслеживания
    pts = cv2.boxPoints(rotatedWindow)
    pts = np.int32(pts)

    cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

    #Показываем результат
    cv2.imshow("Camshift", frame)

    #Выход при нажатии ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

    frame_count += 1

#Метрики
elapsed_time = time.time() - start_time
fps_avg = frame_count / elapsed_time if elapsed_time > 0 else 0
loss_rate = lost_frame_count / frame_count if frame_count > 0 else 0

print(f"Всего обработано кадров: {frame_count}")
print(f"Прошедшее время: {elapsed_time:.2f} секунд")
print(f"Средний FPS: {fps_avg:.2f}")
print(f"Частота потерь: {loss_rate:.2f}")

# Освобождение ресурсов
video.release()
cv2.destroyAllWindows()
