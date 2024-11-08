import cv2 as cv
import cv2

inputv = '/Users/denismalysev/Desktop/dog.mp4'
cap = cv2.VideoCapture(inputv)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

outputv = '/Users/denismalysev/Desktop/lab1/dog2.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(outputv, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

