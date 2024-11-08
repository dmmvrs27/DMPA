import cv2 as cv
import cv2

def readIPWriteTOFile():
    video = cv2.VideoCapture(0)

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("/Users/denismalysev/Desktop/video.mp4", fourcc, 25, (width, height))

    while True:
        ret, frame = video.read()
        if not ret:
            print("Не удалось считать кадр.")
            break
        cv2.imshow('Veb', frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    video.release()
    video_writer.release()
    cv2.destroyAllWindows()
readIPWriteTOFile()
