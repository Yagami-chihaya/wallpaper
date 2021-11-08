import sys

sys.path.append('.')

import requests
from lxml import etree
import os

import src.lib.database as db
import src.lib.download as download
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
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
    }
    proxies = {

    }

    response = requests.get(url=url, params=parmas, headers=headers, proxies=proxies).text
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

        sleep(2)  # 限制爬虫速度
        picture_web = requests.get(url=picture_src, headers=headers).text
        print(picture_web)
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
    '''
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
    update(10, '110', '1w')'''
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
