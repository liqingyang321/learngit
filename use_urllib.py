#! /usr/bin/env python
#coding=utf-8

#urlopen

#import urllib
#urllib.urlopen(url,[,data[,proxies]])
#创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据。

#urlopen返回一个类文件对象，提供以下方法：read(),readlines(),readline(),fileno(),close()
#这些方法和文件对象一样
#info()：返回一个httplib.HTTPMessage 对象，表示远程服务器返回的头信息
#getcode()：返回Http状态码。如果是http请求，200表示请求成功完成;404表示网址未找到；
#geturl()：返回请求的url；

#例一
from urllib import request
import urllib
url2="http://www.baidu.com/"
sock=request.urlopen(url2)
htmlcode=sock.read()
sock.close()
fp=open("E:/example/123.html",'wb')
# fp.write(htmlcode)
fp.close()

#例二
#urlopen参数可以传入一个request请求，其实就是Request类的实例，
#from urllib import request
req=request.Request('http://python.org/')
response=request.urlopen(req)
the_page=response.read()

#urlretrieve()
# urllib.request.urlretrieve(url,'E:/example/abc.html')

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
# request.urlretrieve(url2,local,callbackfunc)

print('parse')
#urlencode,quote,unquote，当url地址有中文或/时需要urlencode编码转换
#urlencode的参数是字典，将key-value转为想要的格式
import urllib
data={'name':'wang','age':'/','addr':'asd'}
urllib.parse.urlencode(data)

#如果只想对一个字符串进行urlencode转换，用quote(),quote_plus()
urllib.parse.quote('hahaha你好啊！')
urllib.parse.quote('a&b/c')#对斜杠进行编码，quote不编码斜杠

#unquote,unquote_plus（把加号解码成空格）
urllib.parse.unquote("hahaha%E4%BD%A0%E5%A5%BD%E5%95%8A%EF%BC%81")
#unquote()函数输出是对应中文在GBK编码下，所谓urlencode就是把字符串转成gbk编码，当终端为utf8编码时，要将结果转成utf8

#发送数据POST，GET数据传送
#动态网页，动态地传递参数给它，它做出对应的响应
#数据传送分为POST和GET两种方式
#GET方式是直接以链接形式访问，链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容
#POST则不会在网址上显示所有的参数

print('POST')
from urllib import parse,request
url='https://passport.csdn.net/account/login'
values={'username':'779477922@qq.com','password':'liqingyang123'}
data=parse.urlencode(values).encode('utf-8')#将字典编码
req=request.Request(url,data)
req.add_header('Referer','http://www.python.org/')
response=urllib.request.urlopen(req).read().decode('utf-8')
#print(response)

print('GET方式')
#构建一个带参数的url
values2={'username':'779477922@qq.com','password':'liqingyang123'}
url2='https://passport.csdn.net/account/login'
data=urllib.parse.urlencode(values2)
geturl=url2+'?'+data
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
request2=request.Request(geturl,headers=headers)
reponse2=request.urlopen(request2).read().decode('utf-8')
print(reponse2)

#网站不同意直接上述方式访问，当识别有问题，站点不会响应，为了完全模拟浏览器工作，需要设置headers的属性
#另外，还有对付‘反盗链’的方式，服务器会识别headers的referer是不是他自己，如果不是，有的服务器不会响应，
#所以我们还可以在header里加入referer。
print('referer:')
header2={'User-Agent':'Mozilla/4.0(compatible; MISE 5.5; Windows NT)',
         'Referer':'http://www.zhihu.com/articles'}#referer告诉服务器我是从哪个页面链接过来的

#代理Proxy的设置，设置代理服务器，每隔一段时间换一个代理,这样不会因为访问一个页面时间过多而被禁止访问
print('代理设置：')
enable_proxy=True
proxy_handler=urllib.request.ProxyHandler({"http":'http://some-proxy.com:8000'})
null_proxy_handler=request.ProxyHandler({})
if enable_proxy:
    opener=urllib.request.build_opener(proxy_handler)
else:
    opener=request.build_opener(null_proxy_handler)
request.install_opener(opener)
a=request.urlopen('https://www.baidu.com/').read().decode('utf-8')
#Timeout设置
#设置等待多久超时，为了解决一些网站响应慢而造成的影响。
#(1)
print('超时设置：')
import socket
timeout=2
socket.setdefaulttimeout(timeout)
url='https://www.baidu.com/'
req=request.urlopen(url).read()
#(2)
response3=request.urlopen(url,timeout=10)

#URLError异常处理
#URLError可能产生的原因：
#网络无连接，即本机无法上网；连接不到特定的服务器；服务器不存在
#用try，except捕捉异常
print('异常处理：')
from urllib import error
request4=request.Request('http:/www.xxx.com')
try:
    req3=request.urlopen(request4)
except urllib.error.URLError as e:
    print(e.reason)

#HTTPError:利用urlopen发出一个请求时，服务器上都会对应一个应答对象response，其中它包含一个数字”状态码”
# 举个例子，假如response是一个”重定向”，需定位到别的地址获取文档，urllib将对此进行处理
#其他不能处理的，urlopen会产生一个HTTPError，对应相应的状态吗，HTTP状态码表示HTTP协议所返回的响应的状态
req=urllib.request.Request('http://blog.csdn.net/cqcre')
try:
    request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)

#综上：
req=request.Request('http://blog.csdn.net/cqcre')
try:
    request.urlopen(req)
except error.HTTPError as e:
    print(e.code)
except error.URLError as e:
    print(e.reason)


