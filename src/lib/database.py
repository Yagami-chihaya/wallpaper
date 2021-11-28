import sys

sys.path.append("..")

import pymysql
import src.config.databaseConfig as dbConfig
import json
import src.lib.download as download

# 连接数据库
dbcf = dbConfig.MySQL()
db = pymysql.connect(
    host=dbcf.host,
    user=dbcf.user,
    password=dbcf.password,
    database=dbcf.database,
    charset=dbcf.charset
)

cur = db.cursor()  # 创建游标


def drop_table():
    dropDBsql = 'drop table if exists url_path'
    cur.execute(dropDBsql)
    db.commit()


def create_table():
    createDBsql = 'create table if not exists url_path(pid int auto_increment primary key not null' \
                  ',url varchar(255) not null' \
                  ',category varchar(255) not null' \
                  ',top_range varchar(255)' \
                  ',current_page int not null' \
                  ',pre_url varchar(255) not null' \
                  ',resolution varchar(255) not null);'
    cur.execute(createDBsql)
    db.commit()


def insert_data(url, category, top_range, current_page, pre_url, resolution):
    insertUrlsql = 'insert into url_path(url,category,top_range,current_page,pre_url,resolution) values(%s,%s,%s,%s,%s,%s);'
    cur.execute(insertUrlsql, [url, category, top_range, current_page, pre_url, resolution])
    db.commit()


def show_all_data():
    num = 24*5*10
    show_table_sql = 'select * from url_path where pid<=%s'%num
    cur.execute(show_table_sql)
    result = json.dumps(cur.fetchall())
    print(result)

    return result


def show_data(category, resolution, date, page):
    sql = ''
    if (page == None):
        if (resolution == ''):
            sql = "select * from url_path where category=\'%s\' and top_range=\'%s\'" % (
                category, date)
        else:
            sql = "select * from url_path where category=\'%s\' and resolution=\'%s\' and top_range=\'%s\'" % (
                category, resolution, date)
    else:
        if (resolution == ''):
            sql = "select * from url_path where category=\'%s\' and top_range=\'%s\' and current_page=\'%s\' " % (
                category, date, page)
        else:
            sql = "select * from url_path where category=\'%s\' and resolution=\'%s\' and top_range=\'%s\' and current_page=\'%s\' " % (
                category, resolution, date, page)

    print(sql)
    cur.execute(sql)
    result = json.dumps(cur.fetchall())
    print(result)
    return result


def show_img(pid):
    sql = 'select * from url_path where pid=%s' % pid
    cur.execute(sql)
    result = json.dumps(cur.fetchall())
    print(result)
    return result


def download_data(pid):
    # 根据pid查询数据库
    sql = 'select * from url_path where pid=%s' % pid
    cur.execute(sql)
    # 提取数据
    result = cur.fetchall()
    url = result[0][1]
    categories = result[0][2]
    page = result[0][4]
    # 数据保存本地并返回信息
    return download.download_pictures(url, categories, page, pid)


def set_wallpaper(pid):
    # 根据pid查询数据库
    sql = 'select * from url_path where pid=%s' % pid
    cur.execute(sql)
    # 提取数据
    result = cur.fetchall()
    url = result[0][1]
    categories = result[0][2]
    page = result[0][4]
    # 数据保存本地并返回信息
    return download.set_wallpaper(url, categories, page, pid)
