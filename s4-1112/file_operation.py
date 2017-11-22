#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
#data = open('yesterday',encoding="utf-8").read()
#打开的文件对象 赋一个变量，后续就可以对这个变量进行操作
''''
f = open('yesterday',encoding="utf-8") #文件句柄 这个句柄存在内存中，包括文件所有信息 大小，字符，硬盘位置等等
                                        #统一封装成一个内存变量给了f句柄
                                        #默认 f = open('yesterday','r',encoding="utf-8") 打开是 r 读模式
                                        #想写文件 f = open('yesterday','w',encoding="utf-8") 变为写模式
#f = open('yesterday2','w',encoding="utf-8")
#data = f.read()
#data2 = f.read()
#data = f.write("12")  #这种方式写同一个文件会覆盖以前内容，不是追加 ,如果是新文件名，会直接创建文件写入内容
#print(data)
  #data2没有内容，因为读文件一的时候，光标已经移动到文件最下方，data2读不到内容了，按照光标位置从头向后读

f.write("太阳\n")
f.write("日") #写入一行，光标下移，写入第二行
#结果显示在不同行需要加入 \n

#追加  用 a
f = open('yesterday2','a',encoding="utf-8")
#f.write("123123什么都是\n")
#f.write("四是四十是十")
data = f.read()
print('------read----------',data)
f.close() #最好关闭文件


#读前几行
f = open('yesterday2','r',encoding="utf-8")
#print(f.readline())

#for i in range(2):  #读前2行
#    print(f.readline())

#打印所有行
#低效循环方式，适合小文件
for index,line in enumerate(f.readlines()):  # 注意readline 和 readlines的区别    print readlines的时候，是每print一次向下输出一行，这样加入循环就会显示所有行
                 #默认输出是有空格和换行符的，strip一下就会吧换行和空格都去掉 显示结果是连贯的

    #print(f.readline)
    if index > 9:
        print("-------分隔符---------")
        break
    print(index,line.strip())   #打印文件前10行
# f.readlines 只适合读小文件，文件超过几个G，需要先把文件读出加载到内存，内存撑爆。。。

#一行一行的读，内存中只保存一行，就不会有内存撑满的问题

#高效循环方式    一行一行的读，内存中只保存一行，就不会有内存撑满的问题  只记住这一种方式
f = open('yesterday2','r',encoding="utf-8")
count = 0
for line in f:
    if count == 9:
        print("----分隔符----")
        count+=1
        continue  #or break
    print(line.strip())
    count+=1

f.close()

############################################################################################
f = open('yesterday2','r',encoding="utf-8")
print(f.tell())

print(f.readline())
print(f.readline():
print(f.tell())#显示光标位置，如果第一行为当返回光标不在第一行时，返回为字符下标

f.seek(0) #光标返回第一行行首，无法返回其他地方
print(f.tell()) #打印光标位置，为0

#如果
f.seek(10)
print(f.readline())  #返回第十个字符所在下标，打印，就会把前面的字符截断不显示

f.detach() #程序写一半了，把字符编码变成utf-8可以用到
f.readable() #判断文件是否可读

f.writable() # 判断文件是否可写
'''
f = open('yesterday2','r',encoding="utf-8")
print(f.encoding) #打印文件编码