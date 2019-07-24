#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import path
from flask import Flask,request,render_template, redirect,url_for
from werkzeug import secure_filename
import pymysql
from Register import register

connection = pymysql.connect("localhost", "root", "csss331331", "ecommerce", charset='utf8' )
cursor = connection.cursor(pymysql.cursors.DictCursor)

""" 你的 APPID AK SK """
APP_ID = '16817866'
API_KEY = 'knoeO8eEGIWvLIHuFczaAWlv'
SECRET_KEY = '6SKGY0ExOECGM0fGboDsScrOmAolHCo5'

#注册上传的照片
filepath = '/Users/yanfeng/PycharmProjects/E-commerce/static/uploads/'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = filepath

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/",methods=['GET','POST'])
def upload():
    if request.method=='POST':
        na = request.form["Name"]
        user_id = request.form['ID']
        em = request.form['Email']
        '''
        base_path = path.abspath(path.dirname(__file__))
        upload_path = path.join(base_path,'static/uploads/')
        file_name = upload_path + secure_filename(f.filename)
        f.save(file_name)
        '''
        #添加照片到人脸库
        regi = register(user_id,na,em,'group1',user_id,'group1')
        regi.Create()

        return redirect(url_for('upload'))
    return render_template('upload.html')



@app.route("/query",methods=['GET','POST'])
def query():
    if request.method=='POST':

        regi = register('test', 'test', 'test', 'group1', 'test', 'group1')
        regi.Query()

        return redirect(url_for('query'))
    return render_template('query.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
