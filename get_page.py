# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
from lianjia.login import Lian
import random
import pymongo
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}
# proxy_lists=[
#     '1.82.216.134:80',
#     '211.143.146.235:80',
#     '111.12.82.4:80'
# ]
# ip=random.choice(proxy_lists)
# proies ={'http':'http://'+ip}


class get_data():
    def __init__(self):
        self.url="http://sh.lianjia.com/ershoufang/d"
        self.headers={
             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }

    def conn_mongodb(self):
        client=pymongo.MongoClient('localhost',27017)
        db = client['lianjia']
        return db

    def get_channel(self,url):
        web_data= requests.get(self.url,headers=self.headers)
        page=BeautifulSoup(web_data.text,"html.parser")
        datas= page.select('.info-panel > h2 > a')

        customer_info=self.conn_mongodb().channelurl

        for data in datas:
            channel_url="http://sh.lianjia.com"+data.get('href')

            customer_info.insert_one({'channel': channel_url})


    def get_olink(self):
        for i in range(1,101):
            url="http://sh.lianjia.com/ershoufang/d" + str(i)
            self.get_channel(url)

        print("insert url complete")

    def get_info(self,url):
        build_data=self.conn_mongodb().lian_jia
        web_data= requests.get(url,headers=self.headers)
        try:
            page=BeautifulSoup(web_data.text,"html.parser")

            data={
                'url' : url,
                'title': page.select('.main')[0].get('title'),
                'price': page.select("div[class='mainInfo bold']")[0].text,
                'room':page.select(".room > .mainInfo")[0].text,
                'area' : page.select(".area > .mainInfo")[0].text
            }
            #info_names= page.find_all("span",class_="title")
            infos= page.select(".aroundInfo")
            s=infos[0].text.split()
            m=[]
            n=[]
            for i in range(0,len(s)-6,2):
                m.append(s[i].replace("：",''))
                n.append(s[i+1].replace("：",''))
                # s += (''.join(d.find_parents("td")[0].text.split()))+','
            for i in range(-3,-6,-2):
                m.append(s[i].replace("：",''))
                n.append(s[i+1])

            d=dict(zip(m,n))
            dictMerged=dict(data)
            dictMerged.update(d)
            build_data.insert_one(dictMerged)
            print("done")

        except Exception as err:
            print (err)

    def coll
a=get_data()
url='http://sh.lianjia.com/ershoufang/sh4532066.html'
print(a.get_info(url))