#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>

using namespace cv;
using namespace std;

void processImage(const string& imgPath, int kernelSize, double sigma, int weaks = 75, int strongs = 150);
Mat nonMaximumSuppression(const Mat& length, const Mat& angle);
Mat doubleThresholdFilter(const Mat& img, int weak, int strong);

int main() {
    string imgPath = "dog.jpeg";
    processImage(imgPath, 11, 2, 0, 50);
    return 0;
}

void processImage(const string& imgPath, int kernelSize, double sigma, int weaks, int strongs) {
    // Задание 1: Чтение изображения, перевод в черно-белый и Гауссово размытие
    Mat img = imread(imgPath);
    if (img.empty()) {
        cerr << "Could not open or find the image!" << endl;
        return;
    }

    Mat gray;
    cvtColor(img, gray, COLOR_BGR2GRAY);
    imshow("Gray", gray);

    Mat blur;
    GaussianBlur(gray, blur, Size(kernelSize, kernelSize), sigma);
    imshow("Gauss", blur);

    // Задание 2: Вычисление и вывод матриц длин и углов градиентов
    Mat sobelX, sobelY;
    Sobel(blur, sobelX, CV_64F, 1, 0, 3);
    Sobel(blur, sobelY, CV_64F, 0, 1, 3);

    Mat length, angle;
    cartToPolar(sobelX, sobelY, length, angle, true);

    imshow("Length", length / 255);
    imshow("Angle", angle / 255);

    cout << "Матрица длин градиента:\n" << length << "\n";
    cout << "Матрица углов градиента:\n" << angle << "\n";

    // Задание 3: Подавление немаксимумов
    Mat nonMax = nonMaximumSuppression(length, angle);
    imshow("Non Max", nonMax);

    // Задание 4: Двойная пороговая фильтрация
    Mat filtered = doubleThresholdFilter(nonMax, weaks, strongs);
    imshow("Filter", filtered);

    waitKey(0);
    destroyAllWindows();
}

Mat nonMaximumSuppression(const Mat& length, const Mat& angle) {
    int rows = length.rows;
    int cols = length.cols;
    Mat supp = Mat::zeros(rows, cols, CV_8U);

    for (int i = 1; i < rows - 1; ++i) {
        for (int j = 1; j < cols - 1; ++j) {
            float dir = angle.at<float>(i, j) % 180;

            float* neighbors = new float[2];
            if ((0 <= dir && dir < 30) || (150 <= dir && dir <= 180)) {
                neighbors[0] = length.at<float>(i, j - 1);
                neighbors[1] = length.at<float>(i, j + 1);
            } else if (30 <= dir && dir < 60) {
                neighbors[0] = length.at<float>(i - 1, j + 1);
                neighbors[1] = length.at<float>(i + 1, j - 1);
            } else if (60 <= dir && dir < 120) {
                neighbors[0] = length.at<float>(i - 1, j);
                neighbors[1] = length.at<float>(i + 1, j);
            } else if (120 <= dir && dir < 150) {
                neighbors[0] = length.at<float>(i - 1, j - 1);
                neighbors[1] = length.at<float>(i + 1, j + 1);
            }

            if (length.at<float>(i, j) >= max(neighbors[0], neighbors[1])) {
                supp.at<uchar>(i, j) = static_cast<uchar>(length.at<float>(i, j));
            }
            delete[] neighbors;
        }
    }

    return supp;
}

Mat doubleThresholdFilter(const Mat& img, int weak, int strong) {
    Mat strongs = (img > strong);
    Mat weaks = (img >= weak) & (img <= strong);

    Mat res = Mat::zeros(img.size(), CV_8U);
    res.setTo(255, strongs);
    res.setTo(0, weaks);

    return res;
}
