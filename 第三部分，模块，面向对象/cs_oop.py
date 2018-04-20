#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__heart = 'Normal'

    def shot(self):
        print("%s shooting..."%self.name)

    def got_shot(self):
        print("ah...,%s got shot..."%(self.name))
        self.__heart = 'stop break'
        print("%s's heart is %s"%(self.name,self.__heart))

    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))

r1 = Role('Alex','police','AK47')  # 生成一个角色 Role(r1,'Alex','police','AK47')
r2 = Role('Jack','terrorist','B22') # 生成一个角色

r1.shot()
r2.got_shot()
r1.buy_gun('M4A1')