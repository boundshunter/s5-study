#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''list_1 = [1,4,3,5,6,7,9,7,4,10]
s1 = set(list_1)  #set 将列表变成集合，并排序去重.

list_2 = [2,15,8,7,22,4,70,5,10]
s2 = set(list_2)

list_3 = [3,5,10]
s3 = set(list_3)
#print(s1,s2)
#交集
s_inter = s1.intersection(s2)  #求 s1,s2交集
print(s_inter)

#并集
s_union = s1.union(s2)   #合并去重
print(s_union)

#差集  s1里面有的，s2里面没有的
s_diff = s1.difference(s2)
#差集 s2里面有的，s1里面没有的
s_diff2 = s2.difference(s1)
print(s_diff2)

#子集 谁包含谁
print(s1.issubset(s2))  #不被包含为  说明 1不是2的子集，为false
print(s3.issubset(s1))  # s2被s1包含，3是1的子集，为true
print(s3.issubset(s2))  #s3 不是s2的子集，想看原因如下，查看差集发现s3中有个3在s2中不存在
print(s3.difference(s2))
#父集 谁被谁包含

print(s1.issuperset(s3)) #s1是s3的父集  True
print(s2.issuperset(s3)) #s2是s3的父集  False

#对称差集
print(s1.symmetric_difference(s2))  #s1,s2里面都不存在的。

#
list_3 = [3,5,10]
s3 = set(list_3)
list_4 = [4,6,9]
s4 = set(list_4)
#无交集
print(s3.isdisjoint(s4)) # 判断无交集

#交集
print(list_1 & list_2)
#并集
print(list_1 | list_2)
#差集
list_1 = [1,4,3,5,6,7,9,7,4,10]
s1 = set(list_1)  #set 将列表变成集合，并排序去重.

list_2 = [2,15,8,7,22,4,70,5,10]
s2 = set(list_2)
print(s1)
print(s2)
print(s1 - s2 ) # in list 1 but not in list 2

#对称差集
print(s1 ^ s2)
'''
#对集合增删改查

list_1 = [1,4,3,5,6,7,9,7,4,10]
list_1 = set(list_1)  #set 将列表变成集合，并排序去重.

list_2 = [2,15,8,7,22,4,70,5,10]
list_2 = set(list_2)

list_1.add(100)  #添加一项
print(list_1)
list_1.update([1,100,150,'x']) #注意用[]
print(list_1)

#remove 删除一项  仅可以删除一项
list_1.remove('x')
print(list_1)

#列表  字典  集合  字符 都是使用下列判断方法
#x in a  # 测试 x 是否为 a 的成员

#x not in a # 判断x 是否 不为a的成员

#len(判断长度）

#copy复制
list_2 = list_1.copy()
print(list_2)
#print(s2)
#pop 删除
#print(list_1.pop())  #随机删除一个，并返回删除元素

print(list_1.discard('ddd')) # 删除一个member如果存在set中，如果不存在 do nothing  ### remove 不存在会报错，discard 不会报错
