#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#-------------------------列表generate器
#这个功能很强大但是目前还没有想到用做干什么
import os
print(list(range(1,30)))
#筛选出偶数的1*1的列表
print([x*x for x in range(1,11)])
tsetlist = [x*x for x in range(1,11)]
#generate可以也可以用两个元素两个元素就相当与把所有的交集列出来
print([m+n for m in 'ab' for n in 'bc'])#>>['ab', 'ac', 'bb', 'bc']
#列出当前文件下所有的文件和文件名
print([d for d in os.listdir('.')])
#用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k+'='+v for k,v in d.items()])
#转换成小写
tsetlist = ['Hello', 'World',18, 'IBM', 'Apple']
#print([s.lower() for s in tsetlist])
#把包含数字的list转化为list
#isinstance是判断类型的
print([s.lower() for s in tsetlist if isinstance(s,str)])










