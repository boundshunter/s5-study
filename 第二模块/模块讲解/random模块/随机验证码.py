#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
# 生成6位 有大写字母和数字随机组成的验证码

import random  # 导入 随机模块
chkcode = ''  # 初始化 验证码为空

for i in range(0,6):  # 循环6次
    # print(i)
    current = random.randint(0,6)  # 定义一个值
    # print(current)
    if current == i:  # 定义的值 和循环到的值相等
        chk_tmp = chr(random.randint(66,90))  # chk_tmp= 随机一个大写字母

    else:
        chk_tmp = random.randint(0,9)  # 定义值 和 i 不相等 chk_tmp = 一个随机数字

    chkcode=chkcode+str(chk_tmp)  # 每次循环  chkcode 循环+1
print(chkcode)

