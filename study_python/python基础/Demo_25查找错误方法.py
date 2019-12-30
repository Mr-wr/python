#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import logging
#--------------------------------assert
#简介的来说就是一个if判断成功，直接报错但是错误信息可以自己定
#有个毛用还不是会报错
#列如：
# def fn(s):
#     n = int(s)
#     assert n!=3,'error'
#     print('ok')
#     return 10/n
# fn(3)#》》报错：AssertionError: error
#------------------------------logging
#logging的好处就是可以自己控制显示的级别有四个等级DEBUG\INFO\WARNING\ERROR
#简单的来说就是可以控制他显不显示
#官方解释：当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息
logging.basicConfig(level=logging.INFO)
#
s = '3'
n = int(s)
logging.info('n = %d' % n)#》》INFO:root:n = 3
print(10 / n)
#------------------------pdb
#好像是python的调试器启用的时候可以用单步运行
#但是要用命令来执行
#输入n可以用来单步执行代码
#任何时候都可以用p i的形式来查看代码
#输入退出调试模式





