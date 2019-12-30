#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#----------------------------返回函数
#就是闭包没有别的，又是闭包我*******
def sum(*age):
    def f():
        a = 0
        for i in age:
            a = a + i
        return a
    return f
listf = [1,2,3,4,5,6,7,8,98,12]
c = sum(*listf)
print(c())
#--------------------------------闭包
#重新回顾一下闭包，因为循环中的函数是不会
#运行的，所以等循环全部都结束之后所以i也就变成最后的值了
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
#解决方法在函数的外层在套用一个函数来接收这个变量
# def cumnt():
#     fs = []
#     def c(i):
#         def f():
#             return i*i
#     for i in range(1,4):
#         fs.append(fs.append(c(i)))
#     return fs
# listc = cumnt()
# def counta():
#     fs = []
#     for i in range(1, 4):
#         def a(c):
#             print(c)
#             def f():
#                 return c*c
#             return f
#         fs.append(a(i))#为什么a没有运行
#     return fs
# f6,f2,f3 =count()
# print(f6())
# print(f3())
# print(f2())






