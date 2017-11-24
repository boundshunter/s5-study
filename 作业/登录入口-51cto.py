#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
#user_info="alex:123#jfsu:sjf319726#xixi:summer" #字符串
#从文件读取
import sys
#sys.exit() #退出模块

f=open("user_info.txt",'r')
user_info = f.read()
f.close()

user_list = user_info.split('#') #以#为分隔符序列化成 列表
#print(user_list) #打印字典

user_dict={} #初始化字典
for item in user_list:
    item_list = item.split(':') #以:为分隔符序列化成列表
    user_dict[item_list[0]]=item_list[-1] #把列表初始化入字典 列表0对应名字，-1最后位置对应密码
    #print(item_list)
    #print(item_list[0],item_list[-1])
    #print(item)
    print(user_dict)