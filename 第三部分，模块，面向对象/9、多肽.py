#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

class Animal:
    def __init__(self,name):
        self.name = name

    def talk(self): # 自定义报错
        raise NotImplementedError("subclass must be implement abstract method")

class Dog(Animal):
    def talk(self):
        return "Woof,Woof！"

class Cat(Animal):
    def talk(self):
        return "Meow!"

d = Dog("D1")
c = Cat("C1")

Animal.talk(d)