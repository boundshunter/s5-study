#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

#面向对象  类 --> class


#面向过程   过程 ---> def
#函数式变成  函数 ---> def


def test(x):
    "文档描述"
    x+=1
    return x

#定义函数
def func1():
    "testing"
    print("in the func1")
    return 0

#定义过程
def func2():
    "testing2"
    print("in the func2")

#函数和过程的区别，过程就是没有返回值的函数

x = func1()
y = func2()
print("From func1 retrun: %s" % x)
print("From func2 return: %s" % y)

#结果来看，过程隐式定义了返回值，所以在python中，过程和函数区别不大

#为什么要使用函数：


