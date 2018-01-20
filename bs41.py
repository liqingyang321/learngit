#! /usr/bin/env python
#coding=utf-8

from bs4 import BeautifulSoup

html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=BeautifulSoup(html)#创建BeautifulSoup对象
#BeautifulSoup(markup, "html.parser")Python默认的解析器

#soup=BeautifulSoup(open('index.html'))#用本地HTML创建对象
#将本地HTML文件打开，来创建soup对象

print(soup.prettify())#输出格式化对象内容
print('end')
#将复杂HTML文档转为一个复杂树形结构，每个节点都是python对象，对象分为四种：
#Tag,NavigableString,BeautifulSoup,Comment

#Tag(HTML中的标签)
print(soup.title)
print(soup.a)
print(soup.p)
#title,a,p是标签，但他每次查找的都是标签中第一个符合要求的

#tag有两个重要属性，name和attrs
print(soup.name)#soup的名字就是[ducument]
print(soup.head.name)#其他内部标签，名字即是标签名称
print(soup.a.name)

print(soup.p.attrs)#p标签的所有属性，字典类
print(soup.p['class'])#单独获得某个属性
print(soup.p.get('class'))#利用get方法传入数据名称

#还可以对属性和内容进行修改
soup.p['class']="newclass"
print(soup.p)

#还可以对属性进行删除
del soup.p['class']
print(soup.p)

#获得标签内容之后，想要获得标签内部文字
print(soup.p.string)

#BeautifulSoup对象表示一个文档全部内容，可以把他当作Tag对象，
print(soup.name)
print(soup.attrs)
print('end')
#comment对象是一个特殊的navigabablestring对象，输出内容不包括注释符

#遍历文档树
#.contents
print(soup.head.contents)#将tag的子节点以列表形式输出
#.children
print(soup.head.children)#输出list生成器，用遍历获取内容
for child in soup.body.children:
    print(child)

print('end3')

#所有子孙节点
#.descendants
#他可以对所有Tag的子孙节点进行递归循环
for child in soup.descendants:
    print(child)

#.string属性
#如果一个标签里面没有标签，或只有唯一一个标签，.string会返回标签里面内容
print(soup.head.string)
print(soup.title.string)
#如果标签里面多个标签，则string方法不能确定哪个子节点内容，输出为None

#.strings获取多个内容
for string in soup.strings:
    print(repr(string))
print('end string')
#输出的字符串中可能包括很多空行，用.stripped_strings可以去除多余空白内容
for string in soup.stripped_strings:
    print(repr(string))

#父节点.parent
p=soup.p
print(p.parent.name)
connect=soup.head.title.string
print(connect.parent.name)

#全部父节点
#.parents
connect=soup.head.title.string
for parent in connect.parents:
    print(parent.name)

#兄弟节点，全部兄弟节点
#.next_sibling,.previous_sibling
print(soup.p.next_sibling)
print(soup.p.previous_sibling)

#.next_siblings,.previous_siblings
for sibling in soup.a.next_siblings:
    print(repr(sibling))

#前后节点
# 与 .next_sibling  .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次
#.next_element,.previous_element
print(soup.head.next_element)

#.next_elements,.previous_elements
for element in soup.a.next_elements:
    print(repr(element))

print('搜索文档树')
#搜索文档树
#find_all(name,attrs,recursive,text,**kwargs)
#name为名字为name的tag，最简单的过滤器(1)是字符串
print(soup.find_all('b'))#查找文档中所有的<b>标签

#（2）传正则表达式
#如果传正则表达式为参数，beautifulsoup通过正则表达式的match()来匹配内容，
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

#(3)传列表
print(soup.find_all(['a','b']))#匹配<a>,<b>

#传True
soup.find_all(True)#True可以匹配任何值，可查找到所有tag

print('方法')
#传方法，定义一个只接受一个参数的方法，方法返回True则表示当前元素匹配并被找到，否则返回False
def hasclassbutnoid(tag):
    return (tag.has_attr('class')and not tag.has_attr('id'))#当前元素包含class属性，不包含id属性
print(soup.find_all(hasclassbutnoid))

#keyword参数
print(soup.find_all(id='link2'))

print(soup.find_all(href=re.compile(r'elsie')))#会搜索每个tag的”href”属性

print(soup.find_all(href=re.compile('elsie'),id='link1'))#多个指定名字的参数可以同时过滤tag的多个属性

#在这里我们想用 class 过滤，不过 class 是 python 的关键词,加个下划线就可以
print(soup.find_all("a",class_='sister'))

#有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性
date_soup=BeautifulSoup('<div data-foo="value">foo!<div/>')
#print(date_soup.find_all(data-foo="value"))会报错，
print(date_soup.find_all(attrs={'data-foo':"value"}))

#text参数
#text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True
print(soup.find_all(text="Elsie"))
print(soup.find_all(text=['Tillie','Eisie']))
print(soup.find_all(text=re.compile(r"Dormouse")))

#limit参数：find_all方法会返回所有搜索结构，如果不需要所有结果，可用limit参数限制数量
print(soup.find_all("a",limit=2))

#recursive参数,调用find_all()方法时，会检索所有子孙节点，如果只想搜索tag的直接子节点
#令recursive=False
print(soup.html.find_all('title'))
print(soup.html.find_all('title',recursive=False))
