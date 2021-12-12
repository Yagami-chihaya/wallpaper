import os
import sys

sys.path.append("..")

import re

import cv2 as cv

print(cv.__file__)
import numpy as np
import src.lib.database as db

download_path = 'pictures'


def to_gray(pid):
    filename = db.download_data(pid)
    filepath = download_path + '\\' + filename
    print(filepath)

    newpath = re.sub(r'\.jpg', '_gray.jpg', filepath)
    if not os.path.exists(newpath):
        img = cv.imread(filepath)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 处理原图像为灰度模式

        cv.imwrite(newpath, gray)

    result = re.sub(r'\.jpg', '_gray.jpg', filename)

    return result


def to_gaussianBlur(pid):
    filename = db.download_data(pid)
    filepath = download_path + '\\' + filename
    newpath = re.sub(r'\.jpg', '_blur.jpg', filepath)
    if not os.path.exists(newpath):
        img = cv.imread(filepath)
        blur = cv.GaussianBlur(img, (15, 15), 0)

        cv.imwrite(newpath, blur)
    result = re.sub(r'\.jpg', '_blur.jpg', filename)

    return result


def to_classical(pid):
    filename = db.download_data(pid)
    filepath = download_path + '\\' + filename
    newpath = re.sub(r'\.jpg', '_classic.jpg', filepath)
    if not os.path.exists(newpath):

        img = cv.imread(filepath)

        rows, cols = img.shape[:2]

        # 新建目标图像

        dst = np.zeros((rows, cols, 3), dtype="uint8")

        # 图像怀旧特效

        for i in range(rows):

            for j in range(cols):

                B = 0.272 * img[i, j][2] + 0.534 * img[i, j][1] + 0.131 * img[i, j][0]

                G = 0.349 * img[i, j][2] + 0.686 * img[i, j][1] + 0.168 * img[i, j][0]

                R = 0.393 * img[i, j][2] + 0.769 * img[i, j][1] + 0.189 * img[i, j][0]

                if B > 255:
                    B = 255

                if G > 255:
                    G = 255

                if R > 255:
                    R = 255

                dst[i, j] = np.uint8((B, G, R))

        # 显示图像

        cv.imwrite(newpath, dst)
    result = re.sub(r'\.jpg', '_classic.jpg', filename)

    return result
