#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import threading
#-----------------------local_school
#local_school是一个ThreadLocal对象
# 所以线程对象只要是在这个线程中哪里都可以访问的到
# 创建全局ThreadLocal对象:
# 可以随便local_school.一个名字
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.a
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.a = name
    # local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()












