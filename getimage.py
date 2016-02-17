
#coding=utf-8
import urllib2
import urllib
import re
import os
save_path = "picture\\"
def getHtml(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
    request = urllib2.Request(url,headers=headers)

    page = urllib2.urlopen(request)
    html = page.read()
    return html

# def getImg(html):
#     reg = r'src="(.+?\.jpg)" alt'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     x = 0
#     for imgurl in imglist:
#         print imgurl
#         filname= save_path
#         urllib.urlretrieve(imgurl,filname+'%s.jpg' % x)
#         x+=1

def getImg(html):
    reg = r'src="(.+?\.jpg)" alt'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        imgData = urllib2.urlopen(imgurl).read()
        filname= save_path +'%s.jpg' % x
        x+=1
        print filname
        if os.path.exists(save_path):
            output = open(filname,'wb+')
            output.write(imgData)
            output.close()
            print str(x),"Finished download \n"
html = getHtml("http://www.qiushibaike.com/pic/page/3/")

print getImg(html)