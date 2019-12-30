#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的

'a test module'
def testmodule():
    print(__name__)

def me():
    print('me')

if __name__ =='__main__':
    me()