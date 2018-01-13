#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import sys
# print(__file__)  # 其实返回的是相对路径，如果在linux下执行会发现
#返回绝对路径的方法
# print(os.path.abspath(__file__))  # 返回绝对路径方法
#
# PARENT_DIR = os.path.dirname( (os.path.abspath(__file__)) ) # 返回上一级，
BASE_DIR = os.path.dirname( os.path.dirname( (os.path.abspath(__file__)) ) ) # 两次调用 parent 就返回了 home 目录
# print(PARENT_DIR)  # bin
# print(BASE_DIR)   # Atm
#
sys.path.append(BASE_DIR)
# import conf,core  # 上面 append之后，就可以直接调用 conf 和 core目录了
# from conf import config
from core import main
if __name__ == '__main__':
    main.run()  # 相当于，从 atm目录，使用base_dir 在通过import  conf 和 core ,可以调用其下面的程序，直接通过main(程序名).login()(函数名)调用

