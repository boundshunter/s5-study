#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
#两种实现方法
with open('a.txt','w',encoding="utf-8") as f:
    for i in range(0,10):
        f.write(str(i)+'\n')

with open('a.txt','w',encoding="utf-8") as f:
    i=0
    while i < 10:
        f.write(str(i)+'\n')
        i+=1