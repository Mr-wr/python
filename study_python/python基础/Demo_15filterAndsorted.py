#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#-------------------------filter
#filter和map一样可以传入一个方法这个方法依次作用与传进来的元素
# 通过返回的bool判断这个元素是留还是走
# a = [1,2,3,4,5,5,6,7,8,9]
# def f(n):
#     return n % 2==0
# print(list(filter(f,a)))
# #反转
# print(a[::-1])
#--------------------------sorted
#用key=接收一个函数主要把参数的所有的元素一个一个带入进去在根据某个值来排序
#是一个排序算法还可以用来接受一个函数来接收这个算法
#个人理解通过方法的返回值判断以什么来排序
b = ['c','d','a','L','f']
# #
print(sorted(b,key=str.lower))
#如果要他反转的话可以加另一个函数
#reverse参数是用来倒序输出的
print(sorted(b,key = str.lower,reverse=True))
#根据成绩来排序
L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Zisa', 88)]
def f(s):
    return s[1]
print(sorted(L,key=f,reverse=True))
#自我练习通过items的方法把所有key和value都取出来然后在带入
c = {'cxiao':'fsdf','afan':"4'4",'zhan':'65','li':'92'}
# print(c[1])
def sort(t):
    return t[1]
# print(sorted(c.items(),key=sort,reverse=True))
