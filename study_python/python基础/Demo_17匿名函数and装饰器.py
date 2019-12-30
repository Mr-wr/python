#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#-------------------------------------匿名函数
#来听听官方解释：这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。高是很高大上就是不简洁易懂
#我个人觉得匿名函数就相当与lamdba表达式
#冒号前面就是参数
# print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
# #匿名函数也是一个对象可以通过赋值的方式给一个变量
# tmap = {'adnfi':'asdfkj','fkadsljf':'asdlkfj'}
# listmap = []
# listmap.append(tmap)
# for i in listmap:
#     print('adfkjfa{}'.format(i.get('adnfi','null').replace('a','bbbbbbbb')))
# print(400%100)
#-----------------------------------装饰器
#简单解释一下：就是在不改动原有的代码情况下增加功能
#装饰器个人感觉就是新建了一个方法然后把赋值给了原来的方法名
def decorator(f):
    def newf(a,b):
        print(a,b)
        return f(a,b)
    return newf

@decorator
def de(x,y):
    print(x+y)

de(2,4)





