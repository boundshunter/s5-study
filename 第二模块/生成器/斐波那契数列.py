#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
1,1,2,3,5,8,13,21
def fib(max):
 n,a,b=0,0,1
 while n<max:
     print(b)
     a,b=b,a+b
     n+=1
 return 'ok'

fib(20)