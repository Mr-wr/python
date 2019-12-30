#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
from collections import namedtuple
from collections import OrderedDict
from collections import ChainMap,Counter

#------------------namedatuple
#可以把变成一个tuple

n = namedtuple('q',['x','y'])
p = n(3,4)
# print(p.count())
print(p.x)
#---------------------OrderdDict
#在存储dict的时候key是无序的如果要保持key的顺序可以用orderddict
od = OrderedDict([('a',1),('b',2),('c',3),('d',4)])
#他会按照插入的顺序排序而不是按照key排序
#------------------------ChainMap
#没有看懂
#------------------------Counter
#返回的时一个dict
#计数器
c = Counter()
for i in 'nihaodsffalfjkl':
    c[i] = c[i]+1

print(c)#Counter({'f': 3, 'a': 2, 'l': 2, 'n': 1, 'i': 1, 'h': 1, 'o': 1, 'd': 1, 's': 1, 'j': 1, 'k': 1})





























