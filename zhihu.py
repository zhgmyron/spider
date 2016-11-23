#-*-coding=utf-8
import requests
url1 ='http://ron.dev.revo.pricerunner.com/'
url2 ='http://ron.dev.revo.pricerunner.com/merchant/profile/dashboard-pr.php'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
values = {'username' : 'dev_test@email.com',  'password' : 'test' }
headers = { 'User-Agent' : user_agent }
s= requests.session()
request = s.post(url1, data=values,headers=headers)


page = s.get(url2,cookies=requests.cookies,headers=headers)

print (page.text)