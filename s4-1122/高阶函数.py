#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

def add(a,b,f):
    return f(a)+f(b)

res=add(3,-6,abs) # abs 绝对值  -6变6

print(res)
