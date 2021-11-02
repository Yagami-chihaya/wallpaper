import sys
sys.path.append('..')

import time
import requests
import os

headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
    }

def download_pictures(url,categories,page,pid,headers=headers):
    isExists = os.path.exists("pictures")  # 判断是否存在pictures目录，如果没有则创建
    if not isExists:
        os.mkdir("pictures")

    start_time = time.time()

    # 获取图片二进制数据
    picture_data = requests.get(url=url, headers=headers).content

    # 为图片文件命名并保存在本地
    picture_name = "类型_" + categories + " 第" + str(page) + "页 第" + str(pid) + "张图片" + ".jpg"
    picture_path = "./pictures/" + picture_name
    with open(picture_path, "wb") as fp:
        fp.write(picture_data)
        end_time = time.time()
        print(url + "下载完成 大小为:" + str(round(os.path.getsize(picture_path) / 1024 / 1024, 2)) + "M 耗时" + str(
            round(end_time - start_time)) + "秒")
        os.startfile("pictures")
    return url + "下载完成 大小为:" + str(round(os.path.getsize(picture_path) / 1024 / 1024, 2)) + "M 耗时" + str(
            round(end_time - start_time)) + "秒"