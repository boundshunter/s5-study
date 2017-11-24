#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''
f = open("yesterday2",'r',encoding="utf-8")
f_new = open("yesterday2.bak",'w',encoding="utf-8")

#方法1：
for line in f:
    if "雪绒花" in line:
        line = line.replace("雪绒花","小瀚宝")
        f_new.write(line)
    else:
        f_new.write(line)

#方法2：
for line in f:
    if "雪绒花" in line:
        line = line.replace("雪绒花","小瀚宝")
    f_new.write(line)'''

#with 防止打开文件忘记关闭
#为了避免打开文件忘记关闭，可以通过管理上下文，即：
'''
with open('log','r') as f:
    ...
如此方式，当with 代码块执行完毕时，内部会自动关闭释放文件资源

Python2.7后，with又支持同时对多个文件上下文进行管理,如：
3.x支持打开多个文件
with open("log1") as obj_1, open("log2") as obj2:
    pass
'''
with open("yesterday2",'r',encoding="utf-8") as f:

    for line in f:
        print(line)
执行完后，自动close()

#python 建议一行代码不要超过80个字符，所以，当打开多个文件时候，需要换行
with open("yesterday2",'r',encoding="utf-8") as f,\
    open("yesterday2.bak",'w',encoding="utf-8") as f_new:
    ...

