#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
# python标准库 直接import不用安装的就是标准库 ，import getpass ，使用密文密码
import getpass
_username = 'Han'
_password = 'abc'
username = input("username:")
password = getpass.getpass("password:")

if _username == username and _password == password:
    print("Welcome user {_name} login..." .format(_name=username))
else:
    print("Invalid username or password!")

#print(username,password)