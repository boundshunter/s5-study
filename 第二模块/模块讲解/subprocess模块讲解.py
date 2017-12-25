#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import subprocess
# os.system
# os.spawn*
# 逐渐就会被 Subprocess替换掉

# 常用subprocess方法示例
#执行命令，返回命令执行状态 ， 0 or 非0
>>> subprocess.call(["ls","-l"])
total 32
drwxr-xr-x  3 root root 4096 Dec 24 17:49 a
-rw-------. 1 root root 1181 Jul 11  2016 anaconda-ks.cfg
-rw-r--r--. 1 root root 3537 Jun  3  2016 dongao_centos6_initial.sh
-rw-r--r--. 1 root root 8815 Jul 11  2016 install.log
-rw-r--r--. 1 root root 3314 Jul 11  2016 install.log.syslog
drwxr-xr-x  2 root root 4096 Dec 11 14:02 python_test
0
>>> retcode = subprocess.call(["ls","-l"])
total 32
drwxr-xr-x  3 root root 4096 Dec 24 17:49 a
-rw-------. 1 root root 1181 Jul 11  2016 anaconda-ks.cfg
-rw-r--r--. 1 root root 3537 Jun  3  2016 dongao_centos6_initial.sh
-rw-r--r--. 1 root root 8815 Jul 11  2016 install.log
-rw-r--r--. 1 root root 3314 Jul 11  2016 install.log.syslog
drwxr-xr-x  2 root root 4096 Dec 11 14:02 python_test
>>> print(retcode)
0
#执行命令，如果命令结果为0，就正常返回，否则抛异常
>>> subprocess.check_call(["ls", "-l"])
0

#接收字符串格式命令，返回元组形式，第1个元素是执行状态，第2个是命令结果
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')

#接收字符串格式命令，并返回结果
>>> subprocess.getoutput('ls /bin/ls')
'/bin/ls'

#执行命令，并返回结果，注意是返回结果，不是打印，下例结果返回给res
>>> res=subprocess.check_output(['ls','-l'])
>>> res
b'total 0\ndrwxr-xr-x 12 alex staff 408 Nov 2 11:05 OldBoyCRM\n'

#上面那些方法，底层都是封装的subprocess.Popen
poll()
Check if child process has terminated. Returns returncode

wait()
Wait for child process to terminate. Returns returncode attribute.


terminate() 杀掉所启动进程
communicate() 等待任务结束

stdin 标准输入

stdout 标准输出

stderr 标准错误

pid
The process ID of the child process.

#例子
>>> p = subprocess.Popen("df -h|grep disk",stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
>>> p.stdout.read()
b'/dev/disk1 465Gi 64Gi 400Gi 14% 16901472 104938142 14% /\n'

>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')

# 调用subprocess.run(...)是推荐的常用方法，在大多数情况下能满足需求，但如果你可能需要进行一些复杂的与系统的交互的话，你还可以用subprocess.Popen(),语法如下：
p = subprocess.Popen("find / -size +1000000 -exec ls -shl {} \;",shell=True,stdout=subprocess.PIPE)
print(p.stdout.read())
#
# 可用参数：
#
# args：shell命令，可以是字符串或者序列类型（如：list，元组）
# bufsize：指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲
# stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
# preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
# close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。
# 所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
# shell：同上
# cwd：用于设置子进程的当前目录
# env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
# universal_newlines：不同系统的换行符不同，True -> 同意使用 \n
# startupinfo与createionflags只在windows下有效
# 将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等
# 终端输入的命令分为两种：
#
# 输入即可得到输出，如：ifconfig
# 输入进行某环境，依赖再输入，如：python
# 需要交互的命令示例

import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n ')
obj.stdin.write('print 2 \n ')
obj.stdin.write('print 3 \n ')
obj.stdin.write('print 4 \n ')

out_error_list = obj.communicate(timeout=10)
print out_error_list

# subprocess实现sudo 自动输入密码

import subprocess

def mypass():
    mypass = '123' #or get the password from anywhere
    return mypass

echo = subprocess.Popen(['echo',mypass()],
                        stdout=subprocess.PIPE,
                        )

sudo = subprocess.Popen(['sudo','-S','iptables','-L'],
                        stdin=echo.stdout,
                        stdout=subprocess.PIPE,
                        )

end_of_pipe = sudo.stdout

print "Password ok \n Iptables Chains %s" % end_of_pipe.read()