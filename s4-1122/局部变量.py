#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

school = 'Edu' #全局变量正确使用方法
def change_name(name):
    #global school #声明后变为全局变量，不声明就是局部变量   禁用 *********** 不要使用
    school = 'qingniao' #局部变量，只作用在函数内部，要先作用在全局，需要声明一下，global school
    print("before name",name,school)
    name="jfsu"  #局部变量
    print("after name",name)

name='xixi' #全局变量
change_name() #函数调用
print(name)
print(school)

列表，字典，元组，集合，都是可以在局部变量里面改全局变量的