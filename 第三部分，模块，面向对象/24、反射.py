#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

def bulk(self):
    print("%s is woo,woo..."% self.name)

class Dog:
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s"%(self.name,food))

d = Dog("dahuang")

choice = input(">>>:")
# d.eat("shi")
#hasattr(obj,name_str) # 返回True 和 False 存在方法属性则返回True,不存在返回False
                  # 判断一个对象（obj）里是否存在对应的name_attr字符串的方法

#getattr(d,choice) # 根据字符串去获取obj对象里的对应方法的内存地址

if hasattr(d,choice):
    func = getattr(d,choice)
    func("shi") # 传入 food 值

else:
    # setattr(x,'y',v) # 动态的将一个外部方法装配到类中调用 相当于  x,y = v
    # setattr(d,choice,bulk) # d实例的 choice 方法 = bulk
    # d.talk(d)   #于 talk是属于单独的函数，需要将实例化对象传入，使self = d ,才可以调用self.name
                # 为什么使用 talk d实例的 choice 方法 = bulk  (setattr(x,y,v)     x,y = v ，y为传入参数
    # 上面为动态装配一个方法

    # 如何动态装配一个属性

    setattr(d,choice,22)
    print(getattr(d,choice))
    #相当于，定义输入项 xxx = 22


if hasattr(d,choice):  # 为真
    getattr(d,choice)  # 取值
else:
    setattr(d,choice,None) # 为False ，set值
    v = getattr(d,choice) # set之后再get ，然后打印
    print(v)


# 处理不固定参数，用来赋值，将输入的choice 付给 方法名
func = getattr(d,choice)
func(d) # d = self


