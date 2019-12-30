#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#-----------------------for in
#for in 可以用多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for c,v in d.items():
    print(c,'=',v)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
for indexMax in L:
    for i in indexMax:
        print(i)
#可以自动生成一个0-10数组
number = range(10)
print(number)
for i in number:
    print(i)
#--------------------------while
#一样的逻辑