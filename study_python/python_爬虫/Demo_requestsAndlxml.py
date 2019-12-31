#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lxml import etree
import requests

path ="https://blog.csdn.net/it_xf?viewmode=contents"
# 获取源代码
htmldate = requests.get(path)
#源码
htmltext = htmldate.text
#个人理解时结构化
etreehtml = etree.HTML(htmltext)
#使用xpath
content = etreehtml.xpath('//*[@id="mainBox"]/main/div[2]/div/h4/a/text()')

for i in content:
    print(i.replace("\n",""))





