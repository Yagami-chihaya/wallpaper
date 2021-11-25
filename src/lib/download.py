import sys
import getpass

sys.path.append('..')

import time
import requests
import os
import ctypes

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
}
user_name = getpass.getuser()  # 获取当前用户名


def download_pictures(url, categories, page, pid, headers=headers):
    download_path = 'C:\\Users\\' + user_name + '\\Downloads\\pictures'
    isExists = os.path.exists(download_path)  # 判断是否存在pictures目录，如果没有则创建
    if not isExists:
        os.mkdir(download_path)

    start_time = time.time()

    # 获取图片二进制数据
    picture_data = requests.get(url=url, headers=headers).content

    # 为图片文件命名并保存在本地
    picture_name = "\\" + categories + str(page) + str(pid) + ".jpg"
    picture_path = download_path + picture_name
    with open(picture_path, "wb") as fp:
        fp.write(picture_data)
        end_time = time.time()
        print(url + "下载完成 大小为:" + str(round(os.path.getsize(picture_path) / 1024 / 1024, 2)) + "M 耗时" + str(
            round(end_time - start_time)) + "秒")
        os.startfile(download_path)
    return picture_name


def set_wallpaper(url, categories, page, pid, headers=headers):
    isExists = os.path.exists("wallpaper")  # 判断是否存在pictures目录，如果没有则创建
    if not isExists:
        os.mkdir("wallpaper")

    # 获取图片二进制数据
    picture_data = requests.get(url=url, headers=headers).content

    # 为图片文件命名并保存在本地
    picture_name = categories + str(page) + str(pid) + ".jpg"
    picture_path = "wallpaper/" + picture_name
    with open(picture_path, "wb") as fp:
        fp.write(picture_data)

    path = os.getcwd()  # 获取文件绝对路径
    print(path + picture_path)

    ctypes.windll.user32.SystemParametersInfoW(20, True, path + '/' + picture_path, 1)
    time.sleep(1)
    os.remove(picture_path)
    os.rmdir('wallpaper')
    return '壁纸设置成功'
