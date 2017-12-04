#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
salary_list = {
    'Alex':100000,
    'Rain':80000,
    'Egon':50000,
    'Yuan':30000
}
# with open('user_info.txt','w',encoding="utf-8") as f_init:
#     f_init.write(str(salary_list))

with open('user_info.txt','r') as f:
    a = eval(f.read())

a.setdefault('Tom','30000')
print(a)
