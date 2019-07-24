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
filepath = '/Users/yanfeng/Downloads/Upload/3.jpeg'

with open(filepath, "rb") as f:
    base64_data = base64.b64encode(f.read())
image = str(base64_data)
imageType = "BASE64"


options = {}
options["quality_control"] = "NORMAL"
options["liveness_control"] = "LOW"
options["action_type"] = "REPLACE"


class register():
    def __init__(self,id, name, email, groupIdList, userId, groupId):
        self.id = id
        self.name = name
        self.email = email
        self.groupIdList = 'group1'
        self.userId = userId
        self.groupId = 'group1'

    def Create(self):
        sql_insert = 'insert into employee' \
                    '(id,name,email)' \
                    'values' \
                    '(\'%s\',\'%s\',\'%s\')' % (self.id, self.name, self.email)

        cursor.execute(sql_insert)
        connection.commit()
        # insert successfully will print this
        print "insert: \'%s\',\'%s\',\'%s\'" % (self.id, self.name, self.email)

        # 在百度人脸库里增加User照片
        client.addUser(image, imageType, self.groupId, self.userId, options)
        add = client.addUser(image, imageType, self.groupId, self.userId, options)
        print add['error_msg']


    def Query(self):
        # 人脸库ID
        res = client.search(image, imageType, self.groupIdList)
        score = res['result']['user_list'][0]['score']
        ID = res['result']['user_list'][0]['user_id']

        if score > 90:
            # print score
            print ID + ' Log in'




