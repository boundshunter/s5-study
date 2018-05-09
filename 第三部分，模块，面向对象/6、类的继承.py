#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''
oop的一个主要功能就是继承
继承有这样一个功能：可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展
通过继承创建的新类称为：“子类”或“原生类”
被继承的类成为“基类”、“父类”或者“超类”
继承的过程就是从一般到特殊的过程

要实现继承，可以通过"继承" （inheritance) 和 "组合"（composition) 来实现
一般情况下，一个子类继承一个父类，要实现多重继承，可以通过多级继承来实现
某些特殊oop情况，一个子类可以继承多个父类（基类）

继承的概念实现方式主要有2类：实现继承、接口继承
·实现继承是指使用基类的属性和方法而无需额外的编码能力
·接口继承是指仅使用属性和方法的名称、但是子类必须提供实现的能力（子类重构父类的方法）

oop开发范式：
划分对象-》抽象类-》将类组织成为层次化结构（继承和合成）->用类与实例进行设计和实现的几个阶段
'''


# 继承示例：
# 没重新就继承父类，重写就使用自己的子类函数
# class Persion(object):
#
#     def talk(self):
#         print("persion is talking.")
#
#
# class BlackPeople(Persion): #继承父类
#     def talk(self): # 重写父类 ，如没有此方法，则继承父类的talk方法
#         print("Blackpeople is talking.")
#     def run(self):
#         print("BlackPeople is running")
#
# b = BlackPeople()
# b.talk()
# b.run()

# 继承在重构 实例：
class person(object):
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        self.sex  = "Normal"
    def talk(self):
        print("person is talking...")

class Blackman(person):
    def __init__(self,name,age,strength): # 先继承，再重构
        person.__init__(self,name,age)  # 继承

        self.strength = strength  # 重构
        print(self.name,self.age,self.sex,self.strength)

    def run(self):
        print("blackman running faster....")

class Whiteman(person):
    def __init__(self,name,age,swim): # 先继承，在重构
        person.__init__(self,name,age) # 继承
        self.swim = swim  # 重构
        print(self.name,self.age,self.swim)
    def swim(self):
        print("whiteman swiming very well.")

b = Blackman('bolte','33','strong')

b.run()

b1 = Whiteman('welpus','29','swim good')

# ******类名要大写******** 基本代码规范

