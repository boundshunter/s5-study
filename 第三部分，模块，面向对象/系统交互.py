#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
#显示当前目录下 文件和目录列表
os.system("dir") # 输出结果到拼命

# popen相当于打开一个内存块，存储
os.popen("dir")  # 存在内存中的值
os.popen("dir").read() # 返回命令的输出结果

#上面两种，只能单一的返回保存结果，或者返回状态
# 如果想即保存返回结果，又能保存返回状态
#需要使用模块
python 2.7 中 command 也可以直线此功能，但是需要在Linux系统中执行

#python 3 中
import subprocess

# subprocess.run() 方法为     python3.5     之后才出现的新方法

#正常使用命令方式
subprocess.run("df",'-h')
# 复杂命令
# 相当于复杂命令，打开shell开关，让shell来解析命令，python不做命令解析了
subprocess.run("df -h |grep data",shell=True)

