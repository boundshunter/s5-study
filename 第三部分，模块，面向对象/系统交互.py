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
subprocess.run(["df",'-h'])
# 复杂命令
# 相当于复杂命令，打开shell开关，让shell来解析命令，python不做命令解析了
subprocess.run("df -h |grep data",shell=True)

#
rel=subprocess.run(["ls","-l"])
返回 CompletedProcess(args=['ls', '-l'], returncode=0)
#
ret=subprocess.call(["ls","-l"])
返回 0或1


subprocess.check_call(["ls","-l"])
命令执行正确，返回0，命令执行不正确抛异常


#接受字符串格式命令，返回元组形式，第一个元素是执行状态，第二个元素是命令结果
subprocess.getstatusoutput("ls /bin/ls")          *********最常用
(0, '/bin/ls')

# 只想获取输出

subprocess.getoutput("ls /bin/ls")
'/bin/ls'


# 上面所有方法，低层都封装了subprocess.Popen()


# 结果存在内存中，要想读出结果到屏幕，需要 stdout=subprocess.PIPE(),否则无法从内存中读出结果
p=subprocess.Popen("ifconfig|grep 110",shell=True,stdout=subprocess.PIPE)
命令为低层封装，必须指定输出到哪，数据不会输出到屏幕，通过PIPE指定，输出到stdout
查看结果
p.stdout.read() # 返回匹配项，

stdout
stdin
stderr

同理，如果报错，想查看错误

p=subprocess.Popen("ifconfig|110",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
出现错误的情况下的输出结果
>>> p.stdout.read()
b''
>>> p.stderr.read()
b'/bin/sh: 110: command not found\n'

需要通过管道输出到stderr做存储，然后做输出

# 检测执行时间较长的程序，如果执行完了，返回0,执行不完返回None
# 不等待结果返回，没执行完直接返回None
#测试
p=subprocess.Popen("sleep 10;echo 'Hello'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(p.poll())

# 等到结果的返回，结果返回后结束
print(p.wait())



# cwd 设置在哪个目录下执行ls命令，返回结果输出为目录下的文件列表 ,**** 不用cd到某个目录下了。
p=subprocess.Popen("ls",shell=True,stdout=subprocess.PIPE,cwd='/tmp')
p.stdout.read()






