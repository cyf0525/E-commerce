# -*- coding: utf-8 -*-
from aip import AipFace
import os
import math
import base64
import pymysql

connection = pymysql.connect("localhost", "root", "csss331331", "ecommerce", charset='utf8' )
cursor = connection.cursor(pymysql.cursors.DictCursor)

""" 你的 APPID AK SK """
APP_ID = '16817866'
API_KEY = 'knoeO8eEGIWvLIHuFczaAWlv'
SECRET_KEY = '6SKGY0ExOECGM0fGboDsScrOmAolHCo5'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
#从服务端获取的照片
filepath = '/Users/yanfeng/PycharmProjects/E-commerce/static/uploads/' + os.listdir('/Users/yanfeng/PycharmProjects/E-commerce/static/uploads/')[0]

with open(filepath, "rb") as f:
    base64_data = base64.b64encode(f.read())
image = str(base64_data)
imageType = "BASE64"

#User ID & Info
userId = 'ddd'
userName = "person3"
userPhone = "12341312"
userEmail = '12332@gmail.com'

def create(id, name, phone, email):
    sql_insert = 'insert into employee' \
                 '(id,name,phone,email)' \
                 'values' \
                 '(\'%s\',\'%s\',\'%s\',\'%s\')' % (id, name, phone, email)

    cursor.execute(sql_insert)
    connection.commit()
    # insert successfully will print this
    print "insert: \'%s\',\'%s\',\'%s\',\'%s\'" % (id,name,phone,email)

#照片库 ID
groupId = 'group1'

options = {}
options["quality_control"] = "NORMAL"
options["liveness_control"] = "LOW"
options["action_type"] = "REPLACE"


# 在Mysql数据库里增加User信息
create(userId,userName,userPhone,userEmail)


# 在百度人脸库里增加User照片
client.addUser(image, imageType, groupId, userId, options)

add = client.addUser(image, imageType, groupId, userId, options)
print add['error_msg']
