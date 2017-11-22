#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = int(input("salary:"))
print(type(salary))
info = '''
------- info of %s -------
Name:%s
Age:%d
Job:%s
Salary:%d
''' % (name,name,age,job,salary)
print(info)

