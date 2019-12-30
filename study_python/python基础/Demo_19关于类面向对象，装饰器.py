#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import types
#-----------------------------类class
#不同的创建类的实例后可以随意添加一个属性,或者方法都可以但是使用实例.的方式创建
#的属性或者方法在其他的实例用不到的,要用类名点的方式添加才能所有的实例才拥有
# class A(object):
#     def __init__(self):
#         pass
# a = A()
# a.name = 'xioam'
# a.age = 19
# a2 = A()
# A.aname = 'Aname'
# print(a2.name)#>>报错
# print(a.name)#>>xioam
# print(a2.aname)#>>Aname
# print(a.aname)#>>Aname
#个人理解————init————：像java中的构造函数但是与其不同的是他的第一个参数一定是self但是传入参数的时候不用传入这个参数（self）
#之后要用self.的形式来赋值变量
#创建类和怎么实例类
# class T_class(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def get_name(self):
#         print(self.name)
#     def get_score(self):
#         print(self.score)
# def f():
#     print('f()')
# student = T_class('xiao',99)
# student.age = 18
# student.t_method = f
# student.get_name()
# student.get_score()
# print(student.age)
# student.t_method()
#-------------------------------------------访问限制
#访问规则:
# 前面有一个下划线的变量实际上可以调用的,但是要把他当作是私有变量不能去调用他(自欺欺人)
# 前面有两个下划线的变量是私有的外界调用不了
# 前后都有两个下划线的变量是特殊变量可以直接访问的
#在python中如果变量前面加上了两个下划线_就是变成了私有模式
# class T_MMGZ(object):
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     def get_name(self):
#         print(self.__name)
#如果在外部调用并赋值有两个下划线的变量其实是新增了一个变量不是调用了实例中的变量
#简洁的来说就是新创建了一个变量并不会覆盖原来的变量
# t = T_MMGZ('xx',18)
# t.__name = 'hh'
# print(t.__name)#>>hh
# t.get_name()#>>xx
#--------------------------------------------继承和多态
#和java的一样
#新知识:鸭子类型:在python中是一个动态语言,
# 在传入参数中不管你传入的是什么类型只要你有这个变量或者有这个方法就可以调用
#不需要考虑是否继承
#简洁的来说局势传入的参数可以不必是指定类型,只要看起来像就可以了
#列如:
# class A(object):
#     def __init__(self):
#         pass
#     def run(self):
#         print('A run')
# class B(A):
#     def __init__(self):
#         pass
# class C(object):
#     def __init__(self):
#         pass
#     def run(self):
#         print('C run')
# def print_run(a):
#     a.run()
# print_run(A())#>>A RUN
# print_run(B())#>>A RUN
# print_run(C())#>>C RUN
#--------------------------------------实例属性和类属性
#在类中也可以定义自己的属性但是所有可以访问的方式都可以访问的到这个属性
#尽量别用和实例相同的变量名因为类属性会被实例民替换掉

#---------------------------------------限制绑定属性__slots__
#限制类的属性
#除了slots中的变量其他的变量都不可可以添加(但是可不可以删除呢?)
#继承的类不会受影响
# class A(object):
#     __slots__ = ('age','name')
#     def __init__(self):
#         pass

#     def run(self):
#         print('A run')
#---------------------------------------装饰器
#第一我很懵逼我是第一次接触这种东西
#我也不知道这种东西的作用是什么
#通过@property的形式可以把方法转换为属性
#简单来说就是有@property的就是相当于get然后又一个对应的setter来设置这个
class A(object):
    def __init__(self):
        pass
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age = value
    @property
    def name(self):
        return 2015
a = A()
a.age = 19
# print(a.age)
#---------------------------------------多重继承
#多重继承就是在后面加个逗号，但是个人觉得如果要多继承尽量不要用太多的类免得结构混乱
# #--------------MixIn
#个人理解在继承中继承是继承父类的，带有MixIn的类是而外的功能
class C(object):
    def __init__(self):
        pass
    def cat(self):
        print('我会cat')
class TMixIn(object):
    def __init__(self):
        pass
    def run(self):
        print('wohuirun')
class Ci(C,TMixIn):
    def __init__(self):
        print('我会c')






















