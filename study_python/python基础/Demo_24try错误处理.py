#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import logging
#---------------------------------try
#和java的一样我就不写了
#---------------------------记录错误logging
#在python中logging可以记录错误信息
#简单的来说就是获取到了错误信息正常运行
#可以通过配置logging可以把错误记录到错误日志里面
#方便以后查询
def main():
    try:
        return 10/'0'
    except Exception as e:
        logging.exception(e)

main()
print('end')
#-----------------------------------抛出错误
#可以自己创建一个类继承错误类然后在需要抛出的地方抛出这个类
#通过raise这个
#简易的来说就是java的一个new 一个对应的错误类然后抛出去



























