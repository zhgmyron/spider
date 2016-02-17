#-*- coding: UTF-8 -*-
import urllib2
import datetime
import re

from bs4 import BeautifulSoup

starttime = datetime.datetime.now()

url = "https://www.packtpub.com/all"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
request = urllib2.Request(url,headers=headers)

page = urllib2.urlopen(request).read()

soup_packtpage = BeautifulSoup(page, "html5lib")


endtime = datetime.datetime.now()
print (endtime - starttime)

starttime = datetime.datetime.now()

all_book_title = soup_packtpage.find_all("div", class_="book-block-title")
all_block = soup_packtpage.find_all("div", class_="book-block")


for b in all_block:
	print("Book's name is " +b.find(class_='book-block-title').string.strip())
	book_price= b.find(class_='book-block-price ')
	print book_price.get_text().strip()

	print("\n")
endtime = datetime.datetime.now()

print (endtime - starttime)

