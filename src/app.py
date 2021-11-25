import sys
sys.path.append('.')


from flask import Flask
from flask import request
import picture as main
import lib.database as db
import lib.imgHandle as h
import lib.check_sexy_img as csi
import os



app = Flask(__name__)

@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ

@app.route('/')
def welcome():
    return '欢迎使用本接口'

@app.route('/updateall')
def update_all_data():
    main.update_all()
    return '更新数据库成功'

@app.route('/showalldata')
def show_all_data():
    return db.show_all_data()

@app.route('/showdata')
def show_data():
    category = request.args.get('category')
    resolution = request.args.get('resolution')
    date = request.args.get('date')
    page = request.args.get('page')
    return db.show_data(category,resolution,date,page)

@app.route('/showimg')
def show_img():
    pid = request.args.get('pid')
    return db.show_img(pid)

@app.route('/download')
def download_data():
    pid = request.args.get('pid')

    return db.download_data(pid)

@app.route('/checkfile')
def check_file():
    os.startfile("pictures")
    return '查看成功'

@app.route('/setwallpaper')
def set_wallpaper():
    pid = request.args.get('pid')
    return db.set_wallpaper(pid)

@app.route('/to_gray')
def to_gray():
    pid = request.args.get('pid')
    return h.to_gray(pid)

@app.route('/to_gaussianBlur')
def to_gaussianBlur():
    pid = request.args.get('pid')
    return h.to_gaussianBlur(pid)

@app.route('/to_classical')
def to_classical():
    pid = request.args.get('pid')
    return h.to_classical(pid)

@app.route('/check_sexy')
def check_sexy():
    pid = request.args.get('pid')
    return csi.check(pid)

if __name__ == '__main__':
    app.run()

