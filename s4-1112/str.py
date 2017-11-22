#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
name = "my baby girl is {_girlname},my baby boy age is {_boyage}"
print(name.capitalize()) #首字母大写
print(name.count("my"))  #统计my出现次数
print(name.center(50,"-"))  # 一共打印50个字符，不足用---补齐，把name值放中间
print(name.endswith("han")) #以han结尾，判定是否正确，正确返回true，判断一个邮件地址是不是以.com结尾等.
print(name.find("y")) #返回字母或单词首字母 首次出现的下标位置。

print(name.format(_girlname="xixi",_boyage=1)) # 传值替换
print(name.format_map( {'_girlname':'xixi','_boyage':1} )) #结果同上 很少用
print(name.isalnum()) #判断是否阿拉伯数字
print('Abc'.isalpha()) #判断字符
print('123'.isalnum()) #是阿拉伯数字为true

print('1'.isdigit())  #判断整数 true
print('asss'.isidentifier()) #判断是不是个合法变量名，不能以符号和数字开头
print('ABC'.islower()) #判断是否小写
print('ABC'.isupper()) #判断是否大写

print('33A'.isnumeric()) # 同 isdigit
print("111 ".isspace()) #判断是否为空格
print('my name is '.istitle()) #判断是否为title， title首字母大写

print('+'.join(['1','2','3','4'])) #将后面字符串中数字，以+拼接
print(name.ljust(50,'*')) #长度50字符，不够用**从右侧补齐  l=left
print(name.rjust(50,'*')) # 左侧补齐  r= right
print('Alex'.upper())
print('JF'.lower())
print('\nJf'.lstrip()) #去掉左边空格、回车
print('\nJf'.rstrip()) #去掉右侧空格、回车
print('Jf'.strip()) # 左右同时去掉

p = str.maketrans("abcdef",'123456')  #abcdef 对应替换 123456
print("Jfeng su".translate(p)) #通过传入替换，把65替换成fe 用p把值对应起来。 做加密对应的，一个对应列表，置换另一段做加密

print('Jfefnfg su'.replace('f','F',2)) #从左往右，把2个f替换成大写F

print('Jfefgeng Sgu'.rfind('g'))  #从左向右数找到最右边第一个出现的g对应下标位置

print('Jfefgeng Sgu'.split('f')) #用f作为分隔符 显示分开后的列表 f可替换为 ，等
print('1+2\n+3+4'.splitlines()) #自动识别换行符 \n
print('Sjf'.swapcase()) # 大小写互换
print('Sjf su jf'.zfill(100)) #显示结果，100个字符，不够用0填充