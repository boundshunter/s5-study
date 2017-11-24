#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''
user_dict = {
    "jfsu":"sjf319726",
    "xixi":"123456",
    "hanhan":"1234!@#",
    "sheyizi":"15210420306",
}

r_in_txt=open("u_dict.txt",'w')
for line in user_dict:
    #print(line,user_dict[line])
    f_write=str(line) +'\t'+ user_dict[line] + '\n'
    r_in_txt.write(f_write)
'''
f=open("u_dict.txt",'r',encoding="utf-8")


