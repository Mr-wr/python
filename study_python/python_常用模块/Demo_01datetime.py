#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
from datetime import datetime,timedelta
#datetime是模块
#-------------------获取当前时间
now = datetime.now()
print('现在',now)
#获取指定的时间
dt = datetime(2019,4,19)
#如果后面的没有会自动补上00
print(type(dt))
#datetime转换为timestamp
tdt = now.timestamp()
print(tdt)
#times转换为datetime
print(datetime.fromtimestamp(tdt))
#timestamp也可以转换成UTC时间
print(datetime.utcfromtimestamp(tdt))
#----------------------str转换为datetime
# zhuan = datetime.strptime('时间','时间格式%Y-%m-%d %H:%M:%S')
#datetime转换str
# strdate = now.strftime('时间格式%a, %b %d %H:%M')
#-----------------------datetime加减
#直接相加减就可以了
print('加10',now+timedelta(hours=10))
print(f'''现在是{now}''')













