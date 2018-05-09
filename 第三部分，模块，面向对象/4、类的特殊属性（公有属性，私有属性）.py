#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# 本实例承接 cs.oop.py

#私有属性
class 默认 内部可访问，外部不可访问

self.__privitename = value

如何使外部只能调用不可修改
再定义一个函数，返回私有属性值
def get_privite(self):
    return self.__privitename

#强制访问 私有属性
# Role 类名，privitename 私有属性名
r1._Role__privitename

# 类里面定义的属性即是 公有属性


