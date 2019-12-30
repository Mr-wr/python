#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#---------------import意思导包
def testReturn(a,b):
    if a>b:
        return a-b,'false'
    return a+b,'true'
#函数返回的是一个tupe
print(testReturn(4,3))
a,b = testReturn(4,3)
print(a,b)







