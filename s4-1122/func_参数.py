#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
def func1(x,y,z):
    print(x)
    print(y)
    print(z)


#x,y为形参，1,2或者z,c为实参数,实参和形参从左到右一一对应,个数不能超过，也不可以少。
#func1(y=3,x=4)
#参数指定值
#func1(x=2,3)
#func1(3,y=2)

#如果没有关键字调用，按照顺序
#有关键字调用，关键参数是不能写在位置参数前面 ,位置参数在前，可以，关键参数在前，位置参数不可用
func1(3,z=2,y=6)

print(func1) #返回在内存中值的位置