#! /usr/bin/env python
#coding=utf-8

#urlopen

#import urllib
#urllib.(url,[,data[,proxies]])
#创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据。

#urlopen返回一个类文件对象，提供以下方法：read(),readlines(),readline(),fileno(),close()
#这些方法和文件对象一样
#info()：返回一个httplib.HTTPMessage 对象，表示远程服务器返回的头信息
#getcode()：返回Http状态码。如果是http请求，200表示请求成功完成;404表示网址未找到；
#geturl()：返回请求的url；

from urllib import request
import urllib
url="http://www.baidu.com/"
sock=request.urlopen(url)
htmlcode=sock.read()
sock.close()
fp=open("E:/example/123.html",'wb')
fp.write(htmlcode)
fp.close()

#urlretrieve()
urllib.request.urlretrieve(url,'E:/example/abc.html')

#直接将远程数据下载到本地
#urllib.urlretrieve(url[, filename[, reporthook[, data]]])
#url:外部或本地url
#filename:文件保存到本地的路径
#reportthook：回调函数，当连接上服务器，以及相应数据块传输完毕时触发该回调函数，可以用来显示当前下载进度
#data:指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。

#将新浪抓取到本地，保存，显示下载进度
from urllib import request
def callbackfunc(blocknum,blocksize,totalsize):
    '''回调函数
    @blocknum:已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent=100.0*blocknum*blocksize/totalsize
    if percent>100:
        percent=100
    print('%0.2f%%' %percent)

url2='http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
local="E:/example/li.html"
request.urlretrieve(url2,local,callbackfunc)