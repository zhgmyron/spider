__author__ = 'zhaor'
#-*-coding=utf-8
import urllib
import urllib2
url ='https://www.zhihu.com/#signin'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
values = {'username' : 'guangking1987@163.com',  'password' : 'Zxcvb1234567' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
request = urllib2.Request(url)
try:
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason

page = response.read()

print page.decode('utf-8')