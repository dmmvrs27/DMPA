import cv2 as cv
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)
    cv2.imwrite("/Users/denismalysev/Desktop/HSVimg.png", hsv)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    if not ret:
        print("Кадр не считан")
        break

cap.release()
cv2.destroyAllWindows()