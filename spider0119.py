#! /usr/bin/env python
#coding=utf-8

#1、爬取简书网站首页文章的标题和文章链接

from urllib import request #url网页地址
from bs4 import BeautifulSoup #从HTML或xml文件中提取结构化数据

#构造头文件，模拟浏览器访问
url='http://www.jianshu.com'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                     '(KHTML,like Gecko) Chrome/55.0.2883.87 SAFARI/537.36'}
page=request.Request(url,headers=header)#抓取网页
page_into=request.urlopen(page).read().decode('utf-8')
#打开url,获取httpresponse返回对象并读取responsebody

soup=BeautifulSoup(page_into,"html.parser")
#将获取的内容转为BeautifuSoup格式，将htmlparser作为html解析工具
#print(soup.prettify())#以格式化的形式打印html

titles=soup.find_all('a','title')

#查找所有a标签中class='title'的语句

with open(r"E:\example\lqy\123.txt",'w') as file:
    for title in titles:
        file.write(title.string+'\n')
        file.write('http://www.jianshu.com'+title.get('href')+'\n\n')
