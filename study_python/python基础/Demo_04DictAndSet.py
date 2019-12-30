#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#--------------------------------------dict(相当于键值对集合)
#dict是无序的对象，对与list查询快但是占用空间多是一个一空间来获取时间
#只能有一个key如果后面又存了key那么会覆盖前面的
testDict = {'zouyishi':8848,'xswl':1451}
print(testDict['xswl'])
#setDefault如果有这key就返回这个value如果没有就增加新的键值对并返回相应的值
testDict.setdefault('zouyishi',45678)
#可以通过in来判断可以是否存在
print('xswl' in testDict)
#通过get来获取数字如果不存在可以用自己的数字或者字符串来带替
print(testDict.get('c','bucun'))
#也可以用pop来获取数据
print(testDict.pop('xswl'))
print(testDict)
#------------------------------------------set
#注意的是在set里面的是list而且这个list是不重复的会自动的过滤出重复的值
#区别：对于dict为一不用的是他没有对应的value
tsetList = [1,2,3,4,5]
testSet = (tsetList,[1,3,])
#通过remove删除某个元素
testSet[1].remove(1)
print(testSet)











