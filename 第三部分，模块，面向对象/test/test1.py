#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# class F1:
#     def __init__(self,n):
#         self.N = n
#         print("F1")
# class F2:
#     def __init__(self,arg1):
#         self.a = arg1
#         print('F2')
# class F3:
#     def __init__(self,arg2):
#         self.a = arg2
#         print("F3")
#
# f1 = F1('a')
# f2 = F2('b')
# # f3 = F3('c')
# while True:
#     num1 = input(">>:")
#     num2 = input(">>:")
class Foo(object):

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        print('func')
        return 'func'

obj = Foo()
# Foo.func("aaa")
# #### 检查是否含有成员 ####
hasattr(obj, 'name')
hasattr(obj, 'func')
#
#### 获取成员 ####
getattr(obj, 'name')
getattr(obj, 'func')
#
#### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)
#
#### 删除成员 ####
# delattr(obj, 'name')
# delattr(obj, 'func')