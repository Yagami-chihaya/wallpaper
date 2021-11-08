import cv2 as cv

def to_gray(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 处理原图像为灰度模式
    cv.imwrite('./gray.jpg', gray)
    return gray