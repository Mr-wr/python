#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
#单个的字符编码
#-----------------------------------------从str》》byte
#------------个人理解python的命名规则
# 在python中我学到了19章类,我才接触到命名规则和类这和我以前学的开篇就介绍命名规则有所不同
#但是我个人认为命名规则还是要放在第一章来讲所以我把这个放在了第一
#命名规则:根据1-19章的知识理解:
# 前面有一个下划线的变量实际上可以调用的,但是要把他当作是私有变量不能去调用他(自欺欺人)
# 前面有两个下划线的变量是私有的外界调用不了
# 前后都有两个下划线的变量是特殊变量可以直接访问的
# 后面下划线的我就不知道了可能19章后面会将
#------------个人理解python的命名规则
print(ord('a'))
#>>97
print(chr(97))
#>>a
#Python对bytes类型的数据用带b前缀的单引号或双引号表示
#通过encode()方法可以编码成指定的bytes
a = 'abc'.encode('ascii')
print(a)#>>b'abc'
print('中文'.encode('utf-8'))#b'\xe4\xb8\xad\xe6\x96\x87'
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
#含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
#print('中文'.encode('ascii'))#报错
#-------------------------------------------从byte>>str
print(b'abc'.decode('ascii'))#》》abc
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))#>>中文
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))#>中
#------------------------------------------------str
print(len('123456789    '))#>>13  空格也算
print(len('abc'.encode('utf-8')))#如果是bytes就算的是字节数一个中文占三个字节
#-----------------------------------------str 格式替换 %、format()
b = 'niaho'
print( 'Hi, %s, you have $.' % b)







