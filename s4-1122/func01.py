#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import time
def logger():
    "增加时间"
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)  #扩展之后，都包含时间打印，易扩展 ，可重复使用
    with open("a.txt","a+",encoding="utf-8") as f:
        f.write("%s end the action \n"% time_current)

def func1():
    print("in the test1")
    logger()

def func2():
    print("in the test2")
    logger()

def func3():
    print("in the test3")
    logger()
func1()
func2()
func3()