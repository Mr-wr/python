#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#----------------------常用函数
#函数名其实就是一个指向对象应用过的名字所以可以当作变量
a = abs
print(a(-234))
#可以用help方法来看
help(abs)
#abs返回正数
print(abs(-4567))
#max可以接受任意的参数并返回最大的那个一个
print(max(1,2,33,4,5,5,6,6,4,43,3,3,4,5))
def mymax(*parameter):
    for id in parameter:
        print(id)
#数据转换int（）
print(int('5678'))
#转化成十六进制的数
print(hex(1))#>>0x1






