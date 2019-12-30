#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#------------------------------生成器
#在python中一遍循环一遍计算的机制就称作为生成器
#在python中只要把】改成）就是了但是不用用平时的print用next来打印
# g = (x*x for x in range(1,10))
# '''for x in g:
#     print(x)'''
#赋值语句
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#a，b = （b，a+b）
#------------------------------yield
#凡是定义了yield就不是一个普通函数了而是一个generator
#定义了yield的方法遇到了yield就返回跟return一样
#会返回yield后面的数
# n = 0
# def testyield(max,n):
#     L = [1]
#     while n < max:
#         yield L
#         L=[1]+[L[i]+L[i+1]for i in range(len(L)-1)]+[1]
#         n = n+1
# for t in testyield(10,n):
#     print(t)

# def tyield(a):
#     while a < 3:
#         yield a
#         a = a+1
#     return 'ok'
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# # c = fib(3)
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
# o  = odd()
# next(o)
print('ok')