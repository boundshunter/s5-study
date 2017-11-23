#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
#函数在内部调用自己，就叫递归函数
#1、要有明确的结束条件。
#2、每次进入更深一层递归时，问题的规模相比上次递归都应该有所减少。
#3、递归效率不高，层次过多容易栈溢出，栈内存大小不是无限的，  算法会详细介绍。
#递归最高999次,程序保护机制

def calc(n):
    print(n)
    if int(n/2) > 0: #一直到1/2 =0.5 int 之后为0，所以最后打印 --->:1
       return calc(int(n/2))
    print("--->:",n)
calc(20)



