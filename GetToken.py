# -*- coding: utf-8 -*-

import urllib, urllib2, sys
import ssl


#access toekn =24.473b5d005dad098331fbeb5f936346f6.2592000.1565939884.282335-16817866

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=knoeO8eEGIWvLIHuFczaAWlv&client_secret=6SKGY0ExOECGM0fGboDsScrOmAolHCo5'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print content