#-*- coding: UTF-8 -*-
import urllib2
import re

class BDTB:
    def __init__(self,baseUrl,seeLZ):
        self.baseURL =baseUrl
        self.seeLZ= '?see_lz='+str(seeLZ)
    def getPage(self,pageNum):
        try:
            url = self.baseURL +self.seeLZ +'&pn='+str(pageNum)
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
            request=urllib2.Request(url,headers=headers)
            response = urllib2.urlopen(request)

            return response.read()

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result:

            return result.group(1).strip()
        else:
            return None
baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
print bdtb.getTitle()
#print bdtb.getPage(1).read().decode('utf-8')