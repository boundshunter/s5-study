#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: hanmer
def test(x,y=3):  #默认参数特点:调用函数的时候，默认参数可有可无，非笔传
    print(x)
    print(y)
test(1)

#默认参数特点:调用函数的时候，默认参数可有可无，非笔传
#默认参数用途：比如安装软件，默认勾选的值等；
#           连接数据库端口好，ssh默认端口号等