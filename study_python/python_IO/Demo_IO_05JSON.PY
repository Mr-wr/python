#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import json
#json有两种处理方法
# 1、把字典对象转化为json对象使用带有s的loads()and dumps()
data = {
    'c':{'date':2},
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
json_str = json.dumps(data)
print(type(data))#dict
print(type(json_str))#str
print(data['c']['date'])
dictjson = json.loads(json_str)
print(type(dictjson))#dict
# 2、读取文本中的json对象使用没有带s的load() and dump()
#load 读取  dump写入
#如果数据是str类型的写入文本的数据是这样的 {\"c\": {\"date\": 2},
#数据尽量是dict类型的写入文本才是正常类型
#写入
with open('data.json','w') as f:
    json.dump(data,f)
#读取
with open('data.json','r')as f:
    print(json.load(f))#{'c': {'date': 2}, 'no': 1, 'name': 'Runoob', 'url': 'http://www.runoob.com'}










