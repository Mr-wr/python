#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import os
#------------------------
#查看是什么系统
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# print(os.name)
#环境变量
# print(os.environ)
#---------------------------------操作文件和目录
#合并和拆分的不需要文件真实存
#查看当前目录的绝对路径
# print(os.path.abspath('.'))
#在路劲合成的时候尽量用join因为不同的操作系统不一样
# os.mkdir(os.path.join(os.path.abspath('.'),'Demo_IO_03test.txt'))
#删除目录
# os.rmdir(os.path.join(os.path.abspath('.'),'Demo_IO_03test.txt'))
#同样的道理拆分目录的时候也用方法
# os.path.split()
#可以得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))
#当前目录下所有文件
print([x for x in os.listdir() if os.path.isabs(x)])















