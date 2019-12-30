#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#----------------课外补充
#list还有其他的表达式
#列如：
aaa = [1,2,3,4,5]
bbb = [1,2,3,4,5,6,7]
print(aaa+bbb)#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7]不会覆盖
print(aaa*3)#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#-----------------------------------------------list是一个有序的集合
#list里面的集合可以不同的元素
testList = ['a',123,'c']
test = ['daf','dasf']
#count计算元素出现的次数
testList.count('a')
#extend 添加list元素
test.extend(testList)
print(testList)#>>['a', 123, 'c']
print(testList[0])#>>'a'
#判断list的长度
print(len(testList))#>>3
#可以用-1获取最后一个元素
print(testList[-1])#>>'c'
print(testList[-2])#>>'b'
#追加元素append
testList.append('d')
print(testList)
#删除元素可以用pop(i):i是索引
testList.pop(0)
print(testList)
#---------------------------------tuple元组
#tuple的元素不能改变所以尽量在初始化的时候就赋值变量
#注意
# 1、upe不能改变指的是tuple对那个元素的指向
# 列如:指向了a就不能指向b
#2、如果tuple只有一个元素的时候就还需要添加一个，
#原因：因为只有一个元素的时候和（）有歧义。例如：（1）编译的时候会把他当作是一个number而不是tuple所以要加一个，消除歧义
testTuple = ('a','b',testList)
print(testTuple)
testList.append('add')
print(testTuple)
#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])











