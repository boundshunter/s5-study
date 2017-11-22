#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''
names = ["father","mother","xixi","hanhan"]
print(names)
print(names[0],names[3])
print(names[1:3])
print(names[3])
print(names[-1]) #取最后一个值
print(names[-2:]) #取最后二个值
print(names[0:]) #取所有值
print(names[1:]) #取第一个值向后所有值
print(names[:2]) #取钱两个值

names.append("yeye") #加到最后
print(names[0:])

names.insert(4,"nainai")
print(names[0:])

names.insert(3,"nainai") #第三个位置插入
print(names)

names[3]="didi" #修改
print(names)

#删除的方法
names.remove("didi") #删除弟弟
print(names)

del names[-1] #删除最后一个
print(names)

names.pop()  #默认删除最后一个，如果输入位置则删除相应位置
names.pop(1)
print(names)
print(names)

print(names.index("father")) #打印位置
print(names[names.index("father")]) #既打印位置又打印名字，当有多个人物重名方便辨认

#统计某个人名有多少个
names.append("didi")
names.insert(1,"gege")
names.insert(2,"father")
#names.clear() #清空列表
names.reverse() #列表反转
print(names)

print(names.count("father"))
names.sort() #列表排序 特殊符号在最前，然后数字，然后大写，然后小写，按照ascii顺序排序的

names2=[1,2,3,4]
names.extend(names2) #把names2表合并过阿里，names2还存在

print(names,names2)

del names2  #删除变量names2
print(names,names2)

names=['didi', 'father', 'father', ['sister','brother'],'gege', 'hanhan', 'mother', 'xixi']

names2=names.copy()
print(names)
print(names2)

names[2]="爸爸"
names[3][0]="姐姐" #浅copy  在copy第二层的时候，copy的只是一个内存地址，不是实际数据
                   #所以当第二层数据改变的时候，内存地址的指向变了，copy的数据也就跟着变了
                   #同理 改names2的第二层 ，names的也会跟着改变

print(names)
print(names2)

names2[3][1]="哥哥"
print(names)
print(names2)

import copy
names=['didi', 'father', 'father', ['sister','brother'],'gege', 'hanhan', 'mother', 'xixi']

names2=copy.copy(names) #依然是浅copy
names2=copy.deepcopy(names) #深copy 完全独立的数据，不会再随着改变而改变
names[2]="爸爸"
names[3][0]="姐姐"

print(names)
print(names2)

names2[3][1]="哥哥"
print(names)
print(names2)

#循环和切片步长
names=['didi', 'father', 'father', ['sister','brother'],'gege', 'hanhan', 'mother', 'xixi']
print(names[0:-1:2]) #从头到尾，步长为2，显示姓名
print(names[:-1:2]) #同上
for i in names:
    print(i)'''

import copy
person=['name',['deposit',200]]
p1=person[:]
p2=person[:]
print(p1)
print(p2)

p1[0]="sujunfeng"
p2[0]="xiezhili"
print(p1)
print(p2)

p1[1][1]=50
print(p1)
print(p2)