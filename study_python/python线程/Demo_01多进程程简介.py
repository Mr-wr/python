#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Queue
import subprocess
import os,time,random
#--------------------------------进程
#由于Unix/Linux操作系统提供了一个fork函数调用
#他会返回两次会把当前进程复制一份，然后分别在父进程和子进程分别返回
#子进程返回的是0，父进程返回的是子进程的id
# pid = os.fork()
# if pid ==0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#然后以上在Windows并不能运行
#----------------------------------------multiprocessing
#在Windows中
def newprocess(name):
    i = 0
    while i<1000:
        print(i,'<',1000)
        i = i+1
    print('这是我创建的进程')
# if __name__ =='__main__':
#     print('这是住进程%s'% os.getpid)
#     p = Process(target=newprocess,args=('test',))
#     print('住进程start')
#     p.start()
#     i = 0
#     while i<100:
#         print(i,'<',1000)
#         i = i+1
#     p.join()
#     print('住进程end')
#所以在子进程中
#-------------------------------pool
#大量启动子进程，（进程池）
#结果是
# Run task 0 (25840)...
# Run task 1 (12672)...
# Run task 2 (24484)...
# Run task 3 (25856)...
# Task 0 runs 0.27 seconds.
# Run task 4 (25840)...
# Task 3 runs 0.92 seconds.
# Task 1 runs 1.23 seconds.
# Task 2 runs 1.61 seconds.
# Task 4 runs 2.63 seconds.
# All subprocesses done.
#原因当创建的进程只有4个时候但是循环了五次前四次是同时运行的，
#当运行到第五次的时候就没有进程了所以要等待前面的某个进程完成之后在运行
#当pool()默认没有参数的时候就是默认系统的核数来
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     # 模拟运行正在运行
#     time.sleep(1)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     # 等待子进程执行完后继续进行
#     p.join()
#     print('All subprocesses done.')

#--------------------------------subprocess
#子进程nslookup
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)
#-------------------进程间的通信
#通信的方式有很多种其中，提供了Queue、Pipes等多种方式来交换数据。
#queue：
# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()











