#-*- coding: UTF-8 -*-
import urllib
import urllib2
import os

picurl="http://pic.qiushibaike.com/system/avtnew/3000/30009055/medium/20150802005124.jpg"
save_path="picture\\"
imgData = urllib2.urlopen(picurl).read()
print imgData
fileName = save_path + "\\ddd.jpg"

if os.path.exists(save_path):
    output = open(fileName,'wb+')
    output.write(imgData)
    output.close()
    print "Finished download \n"
print fileName
print u"运行完成"
