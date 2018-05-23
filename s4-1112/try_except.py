#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han


# try:
#     fh = open("testfile1", "r")
#     fh.write("这是一个测试文件，用于测试异常!!")
# except FileNotFoundError:
#     print("Error: 没有找到文件或读取文件失败")
# else:
#     print("内容写入文件成功")
#     fh.close()
try:
    fh = open("testfile1", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except FileNotFoundError as e:
    print(e.strerror)
else:
    print("内容写入文件成功")
    fh.close()
# fh = open("testfile1", "r")
# fh.write("这是一个测试文件，用于测试异常!!")