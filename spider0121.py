#! /usr/bin/env python
#coding=utf-8

#抓取百度上面搜索关键词为“王尼玛的体重”的网页

from urllib import request,parse

data={}
data['word']='王尼玛的体重'

url_value=parse.urlencode(data)
url='http://www.baidu.com/s?'
full_url=url+url_value
print(full_url)
data=request.urlopen(full_url).read().decode('utf-8')
print(data)
