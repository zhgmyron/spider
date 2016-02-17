#-*- coding: UTF-8 -*-
__author__ = 'zhaor'

import urllib2
import re
from bs4 import BeautifulSoup
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)

    content = response.read().decode('utf-8')

    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<h2>(.*?)</h2>.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number hidden">(.*?)</span>',re.S)
    items = re.findall(pattern,content)

    for item in items:
        haveImg = re.search("img",item[3])
        print item
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason