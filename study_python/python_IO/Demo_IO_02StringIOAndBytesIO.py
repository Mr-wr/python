#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
from io import StringIO
#-------------------------StringIO
#把string的数据写入内存中
r = StringIO()
r.write('hello')
r.write(' ')
r.write('world!')
print(r.getvalue())
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
     s = f.readline()
     if s == '':
         break
     print(s.strip())
#getvalue查看写入后的数据
#-------------------------BytesIO
#和字符一样











