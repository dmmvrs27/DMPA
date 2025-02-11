import cv2
import numpy as np

i = 0
def main(kernel_size, std, tresh, min_area):
    global i
    i += 1

    video = cv2.VideoCapture('LR5.mov', cv2.CAP_ANY)
    ret, frame = video.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (kernel_size, kernel_size), std)

    #Подготовка записи файла
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #Запись видео в файл
    rec = cv2.VideoWriter( 'LR5_res' + str(i) + '.mp4', fourcc, 25, (w, h))

    #Цикл обработки видео до окончания файла.
    while True:
        old_img = img.copy()
        yes, frame = video.read()
        if not yes:
            break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (kernel_size, kernel_size), std)

        diff = cv2.absdiff(img, old_img)
        thresh = cv2.threshold(diff, tresh, 255, cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contr in contours:
            area = cv2.contourArea(contr)
            if area < min_area:
                continue
            rec.write(frame)
    rec.release()
    print('Обработка завершена.')

kernel_size = 27
std = 50
tresh = 60
min_area = 20
main(kernel_size, std, tresh, min_area)

kernel_size = 3
std = 10
tresh = 60
min_area = 50
main(kernel_size, std, tresh, min_area)

kernel_size = 5
std = 30
tresh = 80
min_area = 100
main(kernel_size, std, tresh, min_area)

kernel_size = 9
std = 50
tresh = 40
min_area = 200
main(kernel_size, std, tresh, min_area)