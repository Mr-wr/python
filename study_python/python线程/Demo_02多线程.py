#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import time,threading
#------------------------------------threading
#current_thread返回的是当前线程的实例
#主线程的名字时MainThread
#和前面所学一样都是传入一个函数然后start开始运行的
# 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
#--------------------------------线程锁Lock
#和java的线程锁道理一样，当不同的两个线程访问同一个实例的时候的问题
#使用lock先创建锁，为了确保这个锁可以释放所以用try，finally来确保一定可以释放锁
#当一个线程访问这个变量的时候，可以用多个线程同时访问这个变量
#那么在进行相减操作的时候可能另外一个线程也在进行相减操作
#那么就会改变这个变量原有的值
# number = 0

# def testLock(n):
#     global number
#     number = number+n
#     number = number-n
    
#     # print(number,threading.current_thread().name)
# def run(n):
#     for i in range(1000000):

#         testLock(n)

# t1 = threading.Thread(target=run,name='t1',args=(3,))
# t2 = threading.Thread(target=run,name='t2',args=(10,))
# t3 = threading.Thread(target=run,name='t3',args=(9,))
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# print(number)#》》19，-4，10
# print('ok')
#-----------------------------加锁lock
#一般都要用try
#因为怕程序运行过程中出现异常，从而锁不能释放而导致死锁
#首先创建锁
lock = threading.Lock()
number = 0
def testLock(n):
    global number
    number = number+n
    number = number-n
    
    # print(number,threading.current_thread().name)
def run(n):
    for i in range(1000000):
        #先把这个锁住
        lock.acquire()
        #因为怕死锁所以加try
        try:
            testLock(n)
        finally:
            #无论如何都释放锁
            lock.release()
t1 = threading.Thread(target=run,name='t1',args=(3,))
t2 = threading.Thread(target=run,name='t2',args=(10,))
t3 = threading.Thread(target=run,name='t3',args=(9,))
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print(number)
#-------------------多核cup
#-------------------------继承Thread实现多线程的方式
class MyThread(threading.Thread):
    def __init__(self,fun,arg=()):
        super(MyThread, self).__init__()
        self.fun = fun
        self.arg = arg
    def run(self):
        self.result = self.fun(*self.arg)
    def getresult(self):
        try:  
            return self.result  
        except Exception as e:  
            return str(e)




























