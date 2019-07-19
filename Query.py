# -*- coding: utf-8 -*-
from aip import AipFace
import pymysql
import os
import math
import base64

connection = pymysql.connect("localhost", "root", "csss331331", "ecommerce", charset='utf8' )
cursor = connection.cursor(pymysql.cursors.DictCursor)

""" 你的 APPID AK SK """
APP_ID = '16817866'
API_KEY = 'knoeO8eEGIWvLIHuFczaAWlv'
SECRET_KEY = '6SKGY0ExOECGM0fGboDsScrOmAolHCo5'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

#需要对比的照片
filepath = "/Users/yanfeng/Downloads/test.jpeg"
with open(filepath, "rb") as f:
    base64_data = base64.b64encode(f.read())
image = str(base64_data)
imageType = "BASE64"

def read(id):
    sql_read = 'select * from employee where id = \'%s\'' % id
    cursor.execute(sql_read)
    data = cursor.fetchall()
    for user in data:
        name = user['name']
        email = user['email']
        phone = user['phone']
    # print user info
    print "User id: %s\nName: %s\nEmail: %s,\nPhone: %s" % (id, name, email,phone)

#可选参数
groupIdList = 'group1'
options = {}
options["max_face_num"] = 1
options["face_type"] = "LIVE"
options["liveness_control"] = "NORMAL"

res = client.search(image, imageType, groupIdList)
score = res['result']['user_list'][0]['score']
ID = res['result']['user_list'][0]['user_id']

if score > 90:
    #print score
    print ID + ' Log in'
    read(ID)


