#-*- coding: UTF-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
page = 3
url = 'http://www.qiushibaike.com/hot/page/' + str(page)+'/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)

    soup = BeautifulSoup(response.read(),"html5lib")

    divs= soup.find_all(class_='article block untagged mb15')
    print divs
    print('#'*50)
    for div in divs:
        print "author: ",div.h2.string
        print "content:",div
        print "fun:    ",div.i.string


        print('-'*50)

   # print soup.find_all(id= re.compile('qiushi_tag_*?'))

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason