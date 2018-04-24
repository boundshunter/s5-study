#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# class Foo(object):
#     def __init__(self,name):
#         self.name = name
#
# f = Foo("abc")

def talk(self):
    print("Hello,%s"%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo',(object,),{'talk':talk,'__init__':__init__})
#装配成类，装配成类的过程类似于建立类，然后将init和talk 变成类的属性方法
# 低层是通过type 把 两个属性方法装配到 类中。
# 过程相当于
'''
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print("Hello %s"%self.name)
'''

f = Foo('al',33) # 类的实例化
f.talk() # 调用类方法


class Foo:
    def __init__(self,name):
        self.name = name
        print("++init++")
    def __new__(cls, *args, **kwargs):
        print("++new++")
        return object.__new__(cls) # 去继承父类的new方法 cls 相当于self ，也就是Foo
f = Foo('alex')
'''
__init__ 是通过__new__来实例化的，new其实是init实例化的隐藏父类
一句话： new 就是用来创建实例的
__new__ 在什么情况下使用？
当需要对实例化进行定制的时候

'''

