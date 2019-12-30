#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#-----------------------------------with
#用这个可以帮助我们关闭流
with open('','r') as f:
    print(f.read())
#建议用read（size）因为不知道文件的大小
#如果是二进制的用’rb‘
#如果要读取非utf-8的要传入参数encoding
with open('','rb',encoding='gbk') as r:
    print(r.read(23))


















