import cv2
import numpy as np

def main():

#Задание 4 - Применить фильтр из 3 задания для двух различных значений
    img = cv2.imread("/Users/denismalysev/Desktop/dog.jpeg", cv2.IMREAD_GRAYSCALE)

    #Матрица 5x5 и стандартное квадратичное отклонение 10
    kernel_size_1 = 5
    std_1 = 10
    img_blur_1 = gauss_blur(img, kernel_size_1, std_1)
    cv2.imshow("Matrix 3x3 and std 10", img_blur_1)

    #Матрица 11x11 и стандартное квадратичное отклонение 30
    kernel_size_2 = 11
    std_2 = 30
    img_blur_2 = gauss_blur(img, kernel_size_2, std_2)
    cv2.imshow("Matrix 7x7 and std 30", img_blur_2)

# ------------------------------------------------------------------------------------------------------------------

#Задание 5 - Размытие Гаусса встроенным методом OpenCV
    kernel_size_4 = 11
    std_4 = 30
    img_blur_cv2 = cv2.GaussianBlur(img, (kernel_size_4, kernel_size_4), std_4)
    cv2.imshow("Standard OpenCV", img_blur_cv2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#------------------------------------------------------------------------------------------------------------------

#Задание 1-2 - построение матрицы Гаусса. Выполнение алгоритмов 1-2
def gauss_kernel(kernel_size, std):
    kernel = np.zeros((kernel_size, kernel_size))
    center = kernel_size // 2
    for i in range(kernel_size):
        for j in range(kernel_size):
            kernel[i, j] = gauss(i, j, std, center, center)
    # Нормализуемое ядро
    non_norm = kernel.copy()
    kernel /= np.sum(kernel)
    return non_norm, kernel

#Функция для вычисления значения функции Гаусса
def gauss(x, y, omega, a, b):
    omega2 = 2 * omega ** 2
    coeff = 1 / (np.pi * omega2)
    exponent = np.exp(-((x - a) ** 2 + (y - b) ** 2) / omega2)
    return coeff * exponent

#Разные размерности матриц
kernel_sizes = [3, 5, 7]
std = 1
for size in kernel_sizes:
    non_norm, kernel = gauss_kernel(size, std)
    print(f"Ненормализованная Матрица Гаусса размера {size}x{size}:")
    print(non_norm)
    print(" ")
    print(f"Нормализованная Матрица Гаусса размера {size}x{size}:")
    print(kernel)
    print(" ")

#------------------------------------------------------------------------------------------------------------------

#Задание 3 - реализация фильтра Гаусса средствами Python
def gauss_blur(img, kernel_size, std):
    _, kernel = gauss_kernel(kernel_size, std)
    return convolution(img, kernel)

#Операция свертки
def convolution(img, kernel):
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2
    img_padded = np.pad(img, pad, mode="constant")
    img_blur = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = img_padded[i:i + kernel_size, j:j + kernel_size]
            img_blur[i, j] = np.sum(region * kernel)

    return img_blur

main()
