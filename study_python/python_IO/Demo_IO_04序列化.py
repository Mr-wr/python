#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import pickle
import json
#--------------------------序列化
#简单的来说在程序运行的时候在程序中修改了值但是
#在重写启动程序的时候那个被修改的值没有变
#-------------把一个对象序列化写入文本
# pickle.dumps(d)返回的是一个bytes可以把这个写入文本
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
f = open('dumps.txt', 'wb')
d = pickle.dump(d,f)
f.close()
#从文件里读取序列化的content
f = open('dumps.txt', 'rb')
d = pickle.load(f)
print(d)
f.close()
#如何把python class变成json对象-------------------------
#将类转换为json对象要先把他转换为dict对象
#一种方法就是通过自己定义一个方法来转换
#第二种利用每个类中都有一个__dict__来调用下面会讲
class A(object):
    def __init__(self):
        # self.__name = 'xiaom'
        # self.__age = 18
        self.name = 'name'
        self.age = 18
    def print_test(self):
        print('test')
a = A()
#--------------------------把类转换为dict以及反转
#第一种
def AtoDict(a):
    return{
        'name':a.name,
        'age':a.age
    }
def aload(a):
    return A()
# print(json.dumps(a,default=AtoDict))#{"name": "xiaom", "age": 18}
#第二种
#然后我发现了一个问题当我把类的属性私有化的时候就变成了这个样子_A__name
#加了_name后变成了{'_name': 'name', '_age': 18}
# print(a.__dict__)#{'_A__name': 'xiaom', '_A__age': 18}
d =json.dumps(a,default=lambda obj:obj.__dict__)
# print(d)#{"_A__name": "xiaom", "_A__age": 18}
#-----------------序列化类写入
f = open('dumps2.txt','wb')
pickle.dump(d,f)
f.close()
#--------------------反序列读取
w = open('dumps2.txt','rb')
loada = pickle.load(w)
w.close()
print(loada)
c = json.loads(loada,object_hook=aload)
print(c.age)

#ensure_ascii默认是true会把中文转换为Unicode如果是false的就打印中文
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
