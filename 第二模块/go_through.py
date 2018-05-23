#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import os

#递归
#目录-》文件,文件夹-》文件，文件夹

dirpath = input("输入你要遍历的目录:")

def getdir(dirpath,level=0):
    level +=2
    if not dirpath:
        dirpath = os.getcwd()
        #默认情况下以当前目录开始

    #取出所有文件和文件夹
    myList = os.listdir(dirpath)
    #os.path.isdir

    for name in myList:
        print('-'*level + '|' + name)
        #这里只是一个相对路径
        name = os.path.join(dirpath,name)
        if os.path.isfile(name):
            getdir(name,level)
getdir(dirpath)

