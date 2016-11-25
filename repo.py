# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
url1 ='http://dev.repo.pricerunner.com/'
url2 ='http://dev.repo.pricerunner.com/repo/logo/index.php'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
data = {
        'account_login_csrf':'98d961cdc6ceebaa444449c710cec106',
        'username':'netonnet',
        'password':'test',
        'submit':'submit'
          }
headers = { 'User-Agent' : user_agent }
s = requests.Session()
request = s.post(url1, data=data,headers=headers)
page =request.text

#print (page)
#print (request.cookies)
r = s.get(url2,headers=headers)

print (r.text)