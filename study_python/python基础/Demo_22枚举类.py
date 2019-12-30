#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#-------------------------------枚举类
#通过.value和.name的方法来获取
from enum import Enum

class Month(Enum):
    Jan = 1
    to = 2

name = Month.Jan.value
# name = Month.to.name
print(name)
for m in Month:
    print(m)
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


















