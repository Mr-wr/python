#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import Demo_18testmodule
#-------------------------------------偏值数
#这个函数就是说可以通过functools.partial这个函数简化我们参的形式比如我们要传入三个参数
#但是有两个参数是固定的那么就可以用functools.partial固定这个两个参数
#列如：


# def int2(x):
#     return int(x, base=2)
# print(int2('0000001'))
# print(int('1234',base=16))

print(Demo_18testmodule.testmodule())
# -------------------------------------------模块介绍
#在 python 用 import 或者 from...import 来导入相应的模块。

# 将整个模块(somemodule)导入，格式为： import somemodule

# 从某个模块中导入某个函数,格式为： from somemodule import somefunction

# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

# 将某个模块中的全部函数导入，格式为： from somemodule import *
#调用不同文件下的模块的时候
#每一个.py文件都是一个模块
#每一个包下面都必须有一个_init_.py文件
#-----------使用模块
#先导入模块，在模块中第一个字符串都别视为文档注释
#还有一个——author——
#在某个模块中有一个特殊的变量--name--当是本模块自己调用的时候值是__main__如果是别的模块调用的时候显示的是调用模块的名字
#我觉得————name--可以用来判断是否是自己运行或者是被调用运行
#-----------作用域
#-xxx--这种的变量是特殊变量，-xxxx是私有变量或者私有函数









