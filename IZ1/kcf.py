import cv2
import numpy as np
from pathlib import Path
import time

#Пути
CURRENT_DIR = Path(__file__).parent
MEDIA_DIR = CURRENT_DIR.parent / Path("media")

#Загружаем видео
video = cv2.VideoCapture(str("video1.mp4"))

#Инициализируем трекер CSRT
tracker = cv2.legacy.TrackerCSRT.create()

#Читаем первый кадр
ret, frame = video.read()

#Инициализируем рамку (bounding box) для отслеживаемого объекта
bbox = cv2.selectROI("Tracking", frame, False)

#Запускаем процесс отслеживания
success = tracker.init(frame, bbox)

frame_count = 0  #Количество обработанных кадров
lost_frame_count = 0  #Количество кадров, на которых трекер потерял объект
start_time = time.time()  #Время начала процесса

while True:
    #Читаем следующий кадр
    ret, frame = video.read()

    #Выход из цикла, если видео завершилось
    if not ret:
        break

    #Обновляем трекер
    success, bbox = tracker.update(frame)

    frame_count += 1  #Увеличиваем счетчик кадров

    #Если объект потерялся, увеличиваем счетчик потерянных кадров
    if success:
        cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])), (0, 255, 0), 2)
    if not success:
        lost_frame_count += 1

    #Отображаем видео в фрейме
    cv2.imshow("KCF", frame)

    if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()
            break

#Метрики
elapsed_time = time.time() - start_time
fps = frame_count / elapsed_time if elapsed_time > 0 else 0
loss_rate = lost_frame_count / elapsed_time if elapsed_time > 0 else 0

print(f"Всего обработано кадров: {frame_count}")
print(f"Прошедшее время: {elapsed_time:.2f} секунд")
print(f"Средний FPS: {fps:.2f}")
print(f"Частота потерь: {loss_rate:.2f} кадров в секунду")

video.release()
cv2.destroyAllWindows()