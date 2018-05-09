#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''
class Person(object):

    # 构造方法 也叫 初始化方法  self 就等于实例化后的 实例
    def __init__(self,name,food):  # 下面 d=Person("jfsu") # 先实例化 相当于 Person(d,'jfsu'),
                              #  将d 穿给self

                              # ***如果 food 想被 say 调用，需要在此处声明，否则只需要在下面相应函数声明即可**
        self.name = name
        # self.food = milk
        #相当于d.name = name
        # 定义类中全局 food
        # self.food = food

    def say(self):          # 将d 传给self
        print("I'm a man,my name is %s"% self.name) # self = d self.name 相当于上面的d.name ,而d.name=name
    def eating(self,food):  # eating(d,food)
        print( "%s eating %s"%self.name,food )

d=Person("jfsu") # 先实例化 相当于 Person(d,'jfsu')
d2=Person("hanhan") # 相当于 Person(d2."hanhan")
print(d) #存于内存
print(d2)
#再去调用功能,输出结果
d.say()  # 相当于 d.say(d)
d2.say() # 相当于 d2.say(d2)

'''


class Per(object):
    def __init__(self,name):
        self.name = name

    def sayHi(self):
        print("My name is %s"%self.name)

    def eat(self,food): # food 为局部变量，如果想被sayHi调用 需要在init中初始化声明
        print("%s is eating %s"%(self.name,food))

d = Per('jfsu')
d.sayHi()

d1 = Per('xixi')
d1.eat('miantiao')