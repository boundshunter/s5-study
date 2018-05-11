#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
class Role(object):
    nationality = 'US' # 共有属性
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

    def __del__(self): #析构函数就是用来做垃圾回收 ,做程序的收尾工作，提示关闭连接回收空间
        print("del....run....",self.name)
# 实例化 ，生成r1,r2的过程就是实例化的过程
r1 = Role('Alex','police','AK47')  # 生成一个角色 Role(r1,'Alex','police','AK47')
r2 = Role('Jack','terrorist','B22') # 生成一个角色


r1.shot()
r2.got_shot()
r1.buy_gun('M4A1')

print(r1.nationality) # 调用公有属性
print(r2.nationality) # 调用公有属性

#公有属性更改
Role.nationality = 'CN' # 通过类更改全局的公有属性
print(r1.nationality) # 调用更改后公有属性
print(r2.nationality) # 调用更改后公有属性

# 更改r1的公有属性
r1.nationality = 'JP' # 通过对象，只更改自己的公有属性

print(r1.nationality) # 调用更改后公有属性
print(r2.nationality) # 调用更改后公有属性


# 析构 ，析构函数就是用来做垃圾回收
# del r1
r1.shot()

# del r2  #为析构r1， 析构其实就是删除这个变量到这个函数的引用关系，并没有删除和释放内存空间只相当于把门牌号摘掉了
        #python 的内存刷新机制，一段时间就去做垃圾回收，（清理没有门牌号的内存数据）
