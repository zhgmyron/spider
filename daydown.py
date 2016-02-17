#-*- coding: UTF-8 -*-

import urllib2

from bs4 import BeautifulSoup


for i in range(1,11):

    url = "http://www.0daydown.com/page/"+str(i)

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
    request = urllib2.Request(url,headers=headers)
    opage = urllib2.urlopen(request)
    page =  opage.read()
    soup_packtpage = BeautifulSoup(page,"html5lib")

    opage.close()
    num = " The Page of: " + str(i)
    print(num)
    print("#"*40)
    for article in soup_packtpage.find_all('article', class_="excerpt"):
        print "Category:".ljust(20),article.header.a.next
        print "Title:".ljust(20),article.h2.string
        print("Pulished_time:".ljust(19)), article.p.find('i', class_="icon-time icon12").next
        print "Note: ",article.p.find_next_sibling().string.encode("GBK", 'ignore')
        print('-'*50)

input()
