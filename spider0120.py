#! /usr/bin/env python
#coding=utf-8

from urllib import request
from bs4 import BeautifulSoup
import re
import time

url="https://www.zhihu.com/question/22918070"
html=request.urlopen(url).read().decode('utf-8')
soup=BeautifulSoup(html,'html.parser')

#print(soup.prettify())
#img标签，class="origin_image zh-lightbox-thumb",以.jpg结尾
links=soup.find_all('img',"origin_image zh-lightbox-thumb",src=re.compile(r'.jpg$'))
for link in links:
    print(link)

path=r'E:\example\lqy\images'#设置图片保存路径
for link in links:
    print(link.attrs['src'])#利用。对标签使用attrs[x]获取x属性值
    #request.urlretrieve(link.attrs['src'],path+'\%s.jpg' %time.time())
    request.urlretrieve(link.get('src'), path + '\%s.jpg' % time.time())
    #使用request.urlretrieve将所有远程链接数据下载到本地
