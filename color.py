
#-*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import MySQLdb
url ='http://html-color-codes.info/color-names/'
r= requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
trs = soup .find_all('tr')
conn=MySQLdb.connect(host="localhost",user="root",passwd="root",db="price",charset="utf8")
for tr in trs:
    style= tr.get('style')
    tds =tr.find_all('td')
    td=[x for x in tds]
    name = td[1].text
    hex = td[2].text
    print name," ",hex," ",style
    #print u'颜色： ', name1, u'颜色值：', hex , u'背景样式：',style
    cursor = conn.cursor()
    sql="insert into mycolor (style,name,hex) values (%s,%s,%s)"
    param=(style,name,hex)
    cursor.execute(sql,param)

conn.commit()
cursor.close()

