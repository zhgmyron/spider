# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import pymongo
import random
import time
class ganji:

    def __init__(self):
        self.headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
                }
        self.proxy_lists=[
            '1.82.216.134:80',
            '211.153.17.151:80',
            '1.82.216.135:80'
        ]
        self.ip=random.choice(self.proxy_lists)
        self.proxies ={'http':'http://'+self.ip}
        self.product_links=[]

    def conn_mongodb(self):
        client=pymongo.MongoClient('localhost',27017)
        db = client['58city']
        return db

    def get_channel(self,url):
        web_data=requests.get(url,headers=self.headers)
        page=BeautifulSoup(web_data.text,'html.parser')
        datas = page.select('dl.fenlei > dt > a')

        customer_info=self.conn_mongodb().channelurl
        customer_info.drop()
        for data in datas:
            channel_url= 'http://sh.ganji.com'+data.get('href')

            customer_info.insert_one({'channel': channel_url})
        print ('update collection  channel url')

    def page_url(self,url):
        web_data = requests.get(url,headers=self.headers)
        time.sleep(2)
        page=BeautifulSoup(web_data.text,"html.parser")
        datas = page.select('tr.zzinfo > td.t > a.t')
        table_name=url.split('/')[-3]

        customer_info=self.conn_mongodb()[table_name]


        for data in datas:
            page_url=data.get('href').split('?')[0]
            print (page_url)
            time.sleep(1)
            data=self.page_info(page_url)
            customer_info.insert_one(data)


        print ('update collection  page url')

    def page_info(self,url):

        web_data = requests.get(url,headers=self.headers,proxies=self.proxies)


        try:
            page=BeautifulSoup(web_data.text,'html.parser')
            data={
                'title':page.select('h1.info_titile')[0].text,
                'look_time': page.select('span.look_time')[0].text,
                'price':page.select('div.price_li > span > i')[0].text,
                'place':page.select('div.palce_li > span > i')[0].text,
                'url':url
            }
            return data
        except Exception as err:
            print (err)
data=ganji()
c=data.conn_mongodb()['channelurl']

print (list(c.find({},{'channel': 1})))
for url in c.find({},{'channel':1}):

    for i in range(2,10):
        time.sleep(2)
        link=url['channel']+'o'+str(i)+'/'
        print (link)
        data.page_url(link)
# url='http://sh.ganji.com/shouji/o3/'
# data.page_url(url)

# c=data.conn_mongodb()
#
# for item in c.channelurl.find():
#     name=item['channel'].split('/')[-2]
#
#     for url in c.name.find('name'):
#         pageurl= url['name']
