# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
url1 ='https://accounts.douban.com/login'
url2 ='https://www.douban.com/'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
data = {'form_email' : '13262972387',
          'form_password' : 'Zxcvb1234567',
         'source':'index_nav',
        'redir':'https://www.douban.com/',
        "login":u'登录'
          }
headers = { 'User-Agent' : user_agent }
s = requests.Session()
request = s.post(url1, data=data,headers=headers)
page =request.text
soup= BeautifulSoup(page,"html.parser")

captchaAddr = soup.find('img',id='captcha_image')['src']
if captchaAddr != None:
    reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
    captchaID = re.findall(reCaptchaID,page)
    urllib.request.urlretrieve(captchaAddr,"captcha.jpg")
    captcha = input('please input the captcha:')
    data['captcha-solution'] = captcha
    data['captcha-id'] = captchaID
    r = s.post(url1,data=data,headers=headers)

r=s.get(url2,headers=headers)
print (r.text)


