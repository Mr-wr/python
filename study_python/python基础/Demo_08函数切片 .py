#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#--------------------------------------切片
#切片【从第几个开始：到第几个】
#如果前面没有写第几个就是默认是第零个开始
#如果后面的没有写就是到最后一位
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
num = list(range(100))
#获取前三位元素包头不包尾
print(L[0:3])
print(num[10:21])
#前十个数
print(num[:10])
#后面十位
print(num[-10:])
#前是个数每两个取一个
print(num[:10:2])
#什么都不写是一复制
num2 = num[:]
print(num2[:10])
#字符串也可以看成一个list所以也可以切片
print('adf'[0:1])
#【】反转
print('abcdefghijklmnopq'[::-1])