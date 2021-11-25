import sys, PIL.Image as Image
sys.path.append('..')

import requests
import src.lib.database as db
import json
import os


def check(pid):
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
    }
    url = json.loads(db.show_img(pid))[0][5]
    picture_data = requests.get(url=url, headers=headers).content
    with open('test.jpg', "wb") as fp:
        fp.write(picture_data)

    img = Image.open('test.jpg').convert('YCbCr')
    os.remove('test.jpg')
    w, h = img.size
    data = img.getdata()
    cnt = 0
    for i, ycbcr in enumerate(data):
        y, cb, cr = ycbcr
        if 86 <= cb <= 117 and 140 <= cr <= 168:
            cnt += 1
    if cnt > w * h * .1:
        print("黄图！")
    else:
        print("差评！")
    print(cnt)
    print(w * h * .1)
    return str(cnt / (w * h * .1))


if __name__ == "__main__":
    check(10)
