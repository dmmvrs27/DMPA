import cv2 as cv
import cv2

#Задание 1-2 Вывести на экран изображение. Протестировать три
#возможных расширения, три различных флага для создания окна и три
#различных флага для чтения изображения.
image_jpg = r'/Users/denismalysev/Desktop/mem.jpg'   # JPEG
image_png = r'/Users/denismalysev/Desktop/dog.png'   # PNG
image_bmp = r'/Users/denismalysev/Desktop/plak.bmp'    # BMP

#JPEG
img1 = cv2.imread(image_jpg, cv2.IMREAD_COLOR)
cv2.namedWindow('JPEG - color', cv2.WINDOW_NORMAL)
cv2.imshow('JPEG - color', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#PNG
img2 = cv2.imread(image_png, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('PNG - gray', cv2.WINDOW_AUTOSIZE)
cv2.imshow('PNG - gray', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#BMP
img3 = cv2.imread(image_bmp, cv2.IMREAD_UNCHANGED)
cv2.namedWindow('BMP - alpha', cv2.WINDOW_FREERATIO)
cv2.imshow('BMP - alpha', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()