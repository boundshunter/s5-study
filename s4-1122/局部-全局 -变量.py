#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
name = ['jfsu','xixi','lili','hanhan']

def change_name():
    print("before inside func:",name)
    name[3] = "suyuhan"
    print("inside func:",name)
change_name()
print("out side func:",name)

#列表，字典，集合，类 都是可以在局部变量里面改全局变量的
#元组本身就不可修改
#只有字符串和整数不可在局部修改

