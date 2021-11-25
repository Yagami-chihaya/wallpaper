import random
import sys

sys.path.append('.')

import requests
from lxml import etree

import lib.database as db

from time import sleep


def request_picture(page, categories, topRange):
    url = "https://wallhaven.cc/search?"
    parmas = {
        "categories": categories,
        "purity": '100',  # 请勿更改
        "topRange": topRange,
        "sorting": "toplist",
        "order": "desc",
        "page": page
    }
    headers = {

    }

    headers_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56 ',
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    ]

    headers["user-agent"] = random.choice(headers_list)
    print(headers["user-agent"])
    proxies = {

    }
    try:
        response = requests.get(url=url, params=parmas, headers=headers, proxies=proxies, timeout=20).text
    except:
        sleep(1)
        response = requests.get(url=url, params=parmas, headers=headers, proxies=proxies, timeout=20).text

    tree = etree.HTML(response)
    pre_pic_list = tree.xpath("//img[@alt='loading']/@data-src")
    resolution_list = tree.xpath("//span[@class='wall-res']/text()")

    pictureList = tree.xpath("//a[@class='preview']")

    print(pictureList)
    print(len(pictureList))
    print(resolution_list)
    print(len(pre_pic_list))
    print("网页读取成功！开始获取壁纸数据！")

    i = 0
    for picture in pictureList:
        print(picture)
        picture_src = picture.xpath("@href")[0]  # 这个是爬取预览图片的地址,fake path!
        print(picture_src)
        headers["user-agent"] = random.choice(headers_list)

        # sleep(.1)  # 限制爬虫速度

        try:
            print("开始获取数据")
            picture_web = requests.get(url=picture_src, headers=headers, timeout=20).text
            print(picture_web)
            newtree = etree.HTML(picture_web)
            # 获取图片真正的地址
            picture_src1 = newtree.xpath("//img[@id='wallpaper']/@src")[0]
        except:
            print("重新获取数据")
            sleep(2)
            try:  # 失败则重新爬取数据

                picture_web = requests.get(url=picture_src, headers=headers, timeout=20).text
                newtree = etree.HTML(picture_web)
                # 获取图片真正的地址
                picture_src1 = newtree.xpath("//img[@id='wallpaper']/@src")[0]
            except:
                print("再次获取数据")
                sleep(2)
                picture_web = requests.get(url=picture_src, headers=headers, timeout=20).text
                newtree = etree.HTML(picture_web)
                # 获取图片真正的地址
                picture_src1 = newtree.xpath("//img[@id='wallpaper']/@src")[0]

        # 添加数据到数据库并提交
        db.insert_data(picture_src1, categories, topRange, page, pre_pic_list[i], resolution_list[i].replace(' ', ''))
        i += 1

        print(picture_src1)


def update(pagetotal, type, date):  # 更新数据库数据
    # 第一个参数代表导入数据库的页数，一页24条
    # 第二个参数0代表关闭 1代表开启 第一个数字对应普通壁纸 第二个数字对应动漫壁纸 第三个数字对应人壁纸
    # 第三个参数代表排序时间  1d-一天 3d-三天 1w-一周 1M-一月 3M-三个月 6M-半年

    # 开始导入数据
    page = 1
    while True:
        if page <= int(pagetotal):

            request_picture(page, type, date)

            page += 1
        else:
            break
    print("更新完成，请在数据库查看！")
    return '运行成功'


def update_all():
    # 新建数据库

    db.drop_table()
    db.create_table()

    update(10, '111', '1y')
    update(10, '100', '1y')
    update(10, '001', '1y')
    update(10, '010', '1y')
    update(10, '110', '1y')
    update(10, '101', '1y')
    update(10, '011', '1y')

    update(10, '111', '1d')
    update(10, '100', '1d')
    update(10, '001', '1d')
    update(10, '010', '1d')
    update(10, '110', '1d')
    update(10, '101', '1d')
    update(10, '011', '1d')

    update(10, '111', '1w')
    update(10, '100', '1w')
    update(10, '001', '1w')
    update(10, '010', '1w')
    update(10, '110', '1w')
    update(10, '101', '1w')
    update(10, '011', '1w')

    update(10, '111', '1M')
    update(10, '100', '1M')
    update(10, '001', '1M')
    update(10, '010', '1M')
    update(10, '110', '1M')
    update(10, '101', '1M')
    update(10, '011', '1M')

    update(10, '111', '3d')
    update(10, '100', '3d')
    update(10, '001', '3d')
    update(10, '010', '3d')
    update(10, '110', '3d')
    update(10, '101', '3d')
    update(10, '011', '3d')

    update(10, '111', '3M')
    update(10, '100', '3M')
    update(10, '001', '3M')
    update(10, '010', '3M')
    update(10, '110', '3M')
    update(10, '101', '3M')
    update(10, '011', '3M')

    update(10, '111', '6M')
    update(10, '100', '6M')
    update(10, '001', '6M')
    update(10, '010', '6M')
    update(10, '110', '6M')
    update(10, '101', '6M')
    update(10, '011', '6M')

    return '更新完成'


if __name__ == "__main__":
    update_all()
