#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
    return 'ok'
g=fib(5)

while True:
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# while True:
#     try:
#         x=next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('Generator return Value:',e.value)
#         break

