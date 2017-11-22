#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
# 方法三
name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = int(input("salary:"))
print(type(salary))
info2 = '''
------- info of {_name} -------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
''' .format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)
#需要使用.format
print(info2)

