#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
from collections.abc import Iterable
#-----------------------------------迭代
#不止可以迭代lsit，tuple还可以迭代别的对象
a = {'a':'1','b':'2','c':'3'}
for key in a:
    print(key)

#如何判断这个对象是否可以迭代
print()





