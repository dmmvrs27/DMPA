import cv2
import numpy as np

def process_image(img, kernel_size, sigma, weaks=75, strongs=150):

    #Задание 1. Реализовать метод, который принимает в качестве строки полный адрес файла
    #изображения, читает изображение, переводит его в черно белый цвет и выводит его на
    #экран применяет размытие по Гауссу и выводит полученное изображение на экран.

    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)

    blur = cv2.GaussianBlur(gray, (kernel_size, kernel_size), sigma)
    cv2.imshow("Gauss", blur)

    #Задание 2. Модифицировать построенный метод так, чтобы в результате вычислялось
    #и выводилось на экран две матрицы – матрица значений длин и матрица значений углов
    #градиентов всех пикселей изображения.

    sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
    length = cv2.magnitude(sobel_x, sobel_y)  # Длины градиента
    angle = cv2.phase(sobel_x, sobel_y, angleInDegrees=True)  # Углы градиентов в градусах

    cv2.imshow("Length", cv2.convertScaleAbs(length))
    cv2.imshow("Angle", cv2.convertScaleAbs(angle))

    print("Матрица длин градиента:")
    print(length)
    print(" ")
    print("Матрица углов градиента:")
    print(angle)

    #Задание 3. Модифицировать метод так, чтобы он выполнял подавление немаксимумов
    #и выводил полученное изображение на экран. Рассмотреть изображение, сделать выводы.
    non_max = non_maximum(length, angle)
    cv2.imshow("Non Max", non_max)

    #Задание 4. Модифицировать метод так, чтобы он выполнял двойную пороговую фильтрацию
    #и выводил полученное изображение на экран.
    filtered = filter(non_max, weaks, strongs)
    cv2.imshow("Filter", filtered)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Метод подавления немаксимумов
def non_maximum(leng, angle):
    row, col = leng.shape
    supp = np.zeros((row, col), dtype=np.uint8)

    angle = angle % 180

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            #Напревление
            dir = angle[i, j]
            if (0 <= dir < 30) or (150 <= dir <= 180):
                near = [leng[i, j - 1], leng[i, j + 1]]
            elif 30 <= dir < 60:
                near = [leng[i - 1, j + 1], leng[i + 1, j - 1]]
            elif 60 <= dir < 120:
                near = [leng[i - 1, j], leng[i + 1, j]]
            elif 120 <= dir < 150:
                near = [leng[i - 1, j - 1], leng[i + 1, j + 1]]

            #Подавление значений
            if leng[i, j] >= max(near):
                supp[i, j] = leng[i, j]

    return supp

#Метод двойной пороговой фильтрации
def filter(img, weak, strong):
    strongs = (img > strong).astype(np.uint8) * 255
    weaks = ((img >= weak) & (img <= strong)).astype(np.uint8) * 0

    res = strongs + weaks
    return res

if __name__ == "__main__":
    img = "dog.jpeg"
    process_image(img, kernel_size=11, sigma=2, weaks=0, strongs=50)
