#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
def func(**dict):
    print(type(dict))
    print(dict)
func(a=1,b=9)
func(m=2,n=1,c=11)


def func(a,b,c):
    print(a,b,c)
#args = (1,3,4)
args = {'a':1,'b':2,'c':3}
func(**args)  # 解包字典，必须**



