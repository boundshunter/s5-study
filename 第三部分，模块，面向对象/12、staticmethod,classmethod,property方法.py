#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# 静态方法：
# @staticmethod

# class Dog:
#     def __init__(self,name):
#         self.NAME=name
#
#     def eating(self,food):
#         print("%s is eating %s"%(self.NAME,food))
#
# d = Dog("chenronghua")
# d.eating("包子")
#
# #加入静态方法之后，剥离和类的关系，只是单纯的是类下面的一个函数，跟类没什么关系，不会自动传入self
# class Dog:
#     def __init__(self,name):
#         self.NAME=name
#     @staticmethod  # 实际上跟类没什么关系了，只是调用的时候需要使用类名
#     def eating(self,food): # self被当做一个参数，实际上eating已经变成一个独立的函数
#         print("%s is eating %s"%(self,food))
#
# Dog.eating("a","b")
# a is eating b

# 静态方法 总结 （用户 ，很少，几乎没有）
    #·只是名义上的归类管理，但是在静态方法中访问不了类或实例中的任何属性

'''
-----------------------------------------------------------------------------------------------------------------------
'''

# 类方法
    # @classmethod (用途，未知）

    # 只能访问类变量，不能访问实例变量 ,类变量是在整个类中定义的变量


'''
------------------------------------------------------------------------------------------------------------


# 属性方法
    # @property
    # 把一个方法变成一个静态属性 （属性不能加() 调用）
    # 作用就是隐藏实现细节，对用户来讲只是简单调用
class Foo:
    def __init__(self,name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s"%(self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print("set to food:",food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("删除完了")

b = Foo("li chuang")
b.eat
b.eat = "baozi"
b.eat # 再次调用 包子传给 self.__food，__food在eat的setter中定义，得到值调用


#




# 航班查询
class Flight(object):
    def __init__(self,name):
        self.flight_name = name


    def checking_status(self):
        print("checking flight %s status " % self.flight_name)
        return  3

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0 :
            print("flight got canceled...")
        elif status == 1 :
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")


f = Flight("CA980")
f.flight_status

f = Flight("CA980")
f.flight_status
# f.flight_status =  2
# # ??  不能修改？ 看下面
#
# ############
'''
class Flight(object):
    def __init__(self,name):
        self.flight_name = name


    def checking_status(self):
        print("checking flight %s status " % self.flight_name)
        return  1


    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0 :
            print("flight got canceled...")
        elif status == 1 :
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter #修改
    def flight_status(self,status):
        status_dic = {
           '0' : "canceled",
           '1' : "arrived",
           '2' : "departured"
                    }
        print("\033[31;1mHas changed the flight status to \033[0m",status_dic.get(status) )

    @flight_status.deleter  #删除
    def flight_status(self):
        print("status got removed...")

f = Flight("CA980")
f.flight_status
f.flight_status =  2 #触发@flight_status.setter
del f.flight_status #触发@flight_status.deleter

# '''