#-*- coding: UTF-8 -*-
import urllib2

from bs4 import BeautifulSoup
for i in range(1,2):

    url = "http://www.0daydown.com/page/"+str(i)

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
    request = urllib2.Request(url,headers=headers)
    page = urllib2.urlopen(request)

    soup_packtpage = BeautifulSoup(page,"html5lib")

    page.close()
    num = " The Page of: " + str(i)
    print(num)
    print("#"*40)
    print soup_packtpage.find('article', class_="excerpt")
    for article in soup_packtpage.find_all('article', class_="excerpt"):

        print "Note: ",article('p',class_='note').get_text()
        print('-'*50)