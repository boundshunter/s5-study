#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: hanmer
'''
def test(*args): #不固定参数
    print(args)

test(1,3,4,5,6)
test(*[1,2,4,5,6,7])  #相当于传了一个元祖 args=tuple([1,2,4,5,6,7])

def test1(x,*args):
    print(x)
    print(args)
test(1,2,3,4,5,6,7)
#有时候函数没想好，这样就多个参数留待以后完善

def test2(**kwargs):
    print(kwargs)
    print(kwargs['name']) #关键字取值
    print(kwargs['age'])
    print(kwargs['sex'])
#把N个关键字参数转换成字典的形式
test2(name="alex",age="22",sex="F",height="180")
test2(**{'name':'alex','age':'15','sex':'FM'})
'''
def test3(name,age=18,*args,**kwargs): #默认参数不能放到最后面，参数组一定放在最后
    print(name)
    print(age)
    print(args)
    print(kwargs)
#test3('alex') # 默认参数不写可以输出，参数组不写默认为空组

test3('alex',uname="jfsu",age=35,sex='f',hobby='tesla')#age默认参数重新复制，name值取第一个，剩下的变成元祖

#*args 接收N个位置参数，转换成元组 无位置参数，为空组
#**kwargs 接受N个关键字参数，转换成字典方式

