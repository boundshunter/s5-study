#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''
return 返回值 ，结束函数
return 可以返回什么样的值，
1、个数，类型， 值都不固定，随意指定
2、
'''

def test1():
    print("in the test1")

def test2():
    print("in the test2")
    return 0

def test3():
    print("in the test3")
    return 1,"hello",['xi','han'],{"dabao":"erbao"}

x=test1()
y=test2()
z=test3()

print(type(x),x)  # 返回值=0 返回none 不定义return 隐式返回 None
print(type(y),y)  #返回值=1 返回 object
print(type(z),z)  #返回值=2 返回元组 tuple 全都包含在一个元组中返回,其实是返回一个值

#为什么要有返回值，它的作用是干嘛 ,后面其他程序逻辑，需要返回值结果进行操作

