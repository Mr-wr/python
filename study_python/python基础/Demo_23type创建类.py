#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#--------------------------------type
#个人理解是一个创建类的一个方法和class A（object）差不多
#有三个参数
def print_name(self,name):
    self._name = name
    print(self._name)
#第一个参数是类的名字
#第二个是要继承的类（注意：第二个参数是要用元组来接收的所以要注意元组的写法）
#第三个参数是要第一个是我个人理解应该是一个实例名字后面跟的是他的方法
type('Student',(object,),dict(student = print_name))
#-------------------------------metaclass
#简要：先理解类怎么来的，通常我们都是先定义类然后在创建类
#而用了这个就可以先创建类在定义，就是说先有了你在有的你爸
#用不到的，不用看





















