#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''import sys
#print(sys.path) #打印环境变量
print(sys.argv[2])  #打印列表第二个参数


import os  #python调用 shell命令
#print(os.name)
#print(os.system(dir))
cmd_result=os.system("dir")  #只执行命令，不保存结果
print("My check:",cmd_result)  #My check: 0  命令执行成功与否状态码 命令输出屏幕就没了
'''
import os
'''
cmd_res = os.popen("dir")
print("My check:",cmd_res)  #输出结果 My check: <os._wrap_close object at 0x00000000021CF320> 内存对象中的地址
'''
'''
cmd_res1 = os.popen("dir").read() #加一个read() 把内存中的存储的对象读取出来
print("My check:",cmd_res1)
'''
#os.mkdir("new_dir")  #在当前目录创建目录 new_dir
os.rmdir("new_dir")  #在当前目录删除 new_dir