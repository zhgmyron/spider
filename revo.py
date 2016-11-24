# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
url1 ='http://dev.revo.pricerunner.com/'
url2 ='http://dev.revo.pricerunner.com/common/user/index.php'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
data = {
        'username':'dev_test@email.com',
        'password':'test',
        'country':'GBR',
        'adapter':'default',
        'submit':'submit'
          }
headers = { 'User-Agent' : user_agent }
s = requests.Session()
request = s.post(url1, data=data,headers=headers)
page =request.text

print (request.cookies)
r = s.get(url2,headers=headers)

print (r)
