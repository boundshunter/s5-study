#!/usr/bin/env python
#__Author__ : Summer
#-*- coding: utf-8 -*-

#__call__方法

class func(object):
    def __call__(self, *args, **kwargs):
        print('alex')

func()() # call 方法的调用方式

# __new__方法，先于__init__


# try except

try:
    L=[1,2,3,4]
    print(L[5])
except IndexError as e:
    print(e)

else: # 没有异常
    print("没有异常")

raise("触发异常")
# 断言
assert type(obj.name) is str
print("断言正确")


