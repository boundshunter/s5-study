#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import random

with open('a.txt','a+',encoding="utf-8") as f:
    for i in range(0,10):
        for i in range(0,10):
            f.write(str(random.randint(0,9))) #追加从0-9 10个随机整数，并且每追加一个换行，4个空格开头
