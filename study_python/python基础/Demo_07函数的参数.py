#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#----------------补充
#在传参数中如果传可以改变的参数进来那么原来的参数也会别改变
#例如：
aaa = ['a','b','c','d']
def f(a):
    a[1] = 'hh'
f(aaa)
print(aaa)#['a', 'hh', 'c', 'd']原来的值被改变了
#同理在传入不可改变的类型时候就不会被改变
#------------------------------------默认参数
#我观察好像传进来的参数好像都是tuple元组不可改变
#其实传参数如果忘记了参数的位置可以用=号来传=号可以不用记住位置
#注意必选参数在前默认的参数在后 必选参数》默认参数》可变参数》关键字参数


#如果默认参数指向一个值的话，那么第二次调用这个方法指向的也是这个值（为什么？）
def a(a=[]):
    a.append('n')
    return a
a()
a()
print(a())#>>>['n', 'n', 'n']
#解决方法
def b(a = None):
    if a is None:
        a = []
    a.append('n')
    return a
b()
b()
print(b())#>>>['n']
#----------------------------------------可变参数
#个人理解就是一个可以变得数据比如任意个任意元素进去
#如果要传一个集合要在前面要加* 号代表把所有的元素传进去
#如果没有加的就是把这个集合传入进去进去之后所有的参数都会一tuple的形式
def c(*number):
    print(number)
#如果是list或者是其他的集合的话
testLsit = [1,2,3,4,5,5,6,7]
#*testList表示把传入一个
def d(*testLsit):
    print(testLsit)#>>([1, 2, 3, 4, 5, 5, 6, 7],)
#输出的是一个tuple元组
d(testLsit)
#---------------------------------------关键字参数
#关键字参数不能和里面的原有的key一样
#关键字参数就是说可以传一个dict字典进去也不定长
#传入的dict原值不会被改变他只是拷贝一份值传入参数
testDict = {'name2':'a','age2':23}
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
    print(kw)
#-----------------------位置参数不必按照顺序来传参
person(age=23,name='c',**testDict)
#-------------------------------受限制的关键字
def person2(name,age,*stud2,name2,age2):
    print(name,stud2,age,name2,age2)

stud2 = {'name2':'afd','age2':'asdlfj'}
person2(name='name',age='age',**stud2)
#----------------------------------参数组合
#参数组合必须按着这样的顺序
#必须参数，默认参数，可变参数，命名参数
