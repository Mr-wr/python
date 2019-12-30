#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#------------------------------------定制类
#------------------------这个一章就是了解类的
#用作java的话就是重写类的方法
#---------__str__
# 的方法就像当与java类中的tostring方法在类中写str方法就是重写了tostring一样
#print()方法就是调用类的__str__方法
# class Student(object):
#     def __init__(self):
#         pass
#     def __str__(self):
#         return 'Student'
# student = Student()
# print(student)
#----------------__iter__
#是一个可以把类变成迭代的一个方式返回的是类本身
class Titer(object):
    def __init__(self):
        self._a,self._b = 1,3
    def __iter__(self):
        return self
    def __next__(self):
        self._a,self._b = self._a,self._b+self._a
        if self._b>100:
            raise StopIteration()
        return self._b
    # 通过下标来获取
    # def __getitem__(self,n):
    #     for i in range(n):
    #         self._a,self._b = self._a,self._b+self._a
    #         return self._b
    # 通过切片的方式来获取
    def __getitem__(self,n):
        #首相判断n的类型
        if isinstance(n,int):
             for i in range(n):
                self._a,self._b = self._a,self._b+self._a
                return self._b
        #如果是切片
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            l = []
            for i in range(stop):
                if i>=start:
                    l.append(self._b)
                self._a,self._b = self._a,self._b+self._a
            return l
    def __call__(self):
            print(self._a)
titer = Titer()
# for i in titer:
#     print(i)#>>4->100

#-------------------__getitem__
#在类中重写这个方法可以让实例类通过下标来访问数据
#但是如果用的是一个切片的类型就要加一个判断
print(titer[:9])
#---------------------__getattr__
#在类调用类中不存在的属性后就会报错
#在类中重写这个方法就不会报错但是缺点是每次都要自己创建
#个人觉得无关紧要
#-------------------__call__
#只要在类中重写这个函数就可以直接进行调用
titer()
#如果有方法和这个类名相同那么我们怎么知道他到底是一个函数类型
#还是一个类对象呢所以我们可以用callable的方法
#-----------------------Callable()
#只要类中重写了__call__的他们都是Callable对象
callable(titer)#》》true
#可以通过这个判断是否是可调用类型


















