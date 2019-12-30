#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
from collections.abc import Iterable,Iterator
#------------------------------Iterable
#凡是可以用于for循环的都可是iterable，凡是用next的都是iterator
#可以被next不断返回下一个的对象称为迭代器iteratior
#可以使用isinstance判断是否是iterator对象
#生成器都是iterator对象但是list、dict，str都不是iterator
#可以使用iter（）把他们转换成iterator对象
print(isinstance(iter([]),Iterator))
print()








