#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os import path
from flask import Flask,request,render_template, redirect,url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/Users/yanfeng/Documents/Upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload",methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f = request.files["file"]
        base_path = path.abspath(path.dirname(__file__))
        upload_path = path.join(base_path,'static/uploads/')
        file_name = upload_path + secure_filename(f.filename)
        f.save(file_name)
        return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
