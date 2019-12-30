#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
from functools import reduce
#------------------------------map
#map搜两个参数一个是函数一个是，iterable，返回的是一个新的iterator
#
# def f(x):
#     return x*x
# testitertor = map(f,[1,2,3,4,5,6,7,8])
# for i in testitertor:
#     print(i)
# #也可以抽象，把所有元素弄成str
# for i in list(map(str,[1,2,3,4,5,6,7,8])):
#     print(i)
#------------------------------------------------reduce
#传入reduce的函数要接收两个参数把两个参数计算后的结果在和下一个元素计算
# def add(x, y):
#      return x+y
# a = reduce(add,[1])
# print(a)

def char2num(s):
     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
     return digits[s]
#因为字符串也是一个序列所以
for k in map(char2num,'2324325'):
    print(k)
#---------------------------------------------------练习map
#练习['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# a = ['adam', 'LISA', 'barT']
# def f(s):
#     return s[0].upper()+s[1:].lower()
# c = list(map(f,a))
# print(c)






