import cv2 as cv
import cv2

cap = cv2.VideoCapture("http://172.20.10.6/video")

if not cap.isOpened():
    print("Не удалось подключиться к камере.")
else:
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Сamera", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            print("Не получилось")
            break

cap.release()
cv2.destroyAllWindows()
