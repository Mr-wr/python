#!/usr/bin/env python3
#告诉linux system this is  execute  procedure
#windows 会忽略这个
# -*- coding: utf-8 -*-
#告诉python解析器是按照utf-8编码的
import threading
import time
from threading import Timer,Thread,Event

class perpetualTimer():
    def __init__(self,t,hFunction,*age):
        self.t=t
        self.hFunction = hFunction
        self.age = age
        self.thread = Timer(self.t,self.handle_function,args=self.age)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()
    def start(self):
        self.thread.start()
    def cancel(self):
        self.thread.cancel()

def printer():
    print ('ipsem lorem')
    t = perpetualTimer(5,printer)
    t.start()
def hello(name):    
    print ("hello %s\n" % name)
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()
    print(time)
if __name__ == "__main__":
    printer()
    # timer = threading.Timer(2.0, hello, ["Hawk"])
    # timer.start()










