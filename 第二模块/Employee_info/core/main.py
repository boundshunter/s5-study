#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# import sys
import datetime
import json

from core import db_handler
from core import auth
from conf import settings

#用户存储在同一个db file 全局路径设置
db_path = db_handler.db_handler(settings.DATABASE)


def run():

    msg = u'''
    \033[32;1m------------操作选项----------
    1、查询用户信息
    2、增加用户
    3、修改用户信息
    4、删除用户
    5、退出
    \033[0m
        '''

    msg_dic = {
        '1':"select()",
        '2':"add()",
        '3':"update()",
        '4':"delete()",
        '5':"log_out()"
    }
    go_flag = True
    while go_flag:
        print(msg)
        user_choice = input("\033[35;1m请输入您的选择>>>:\033[0m")

        if user_choice in msg_dic:
            go_flag = eval(msg_dic[user_choice])

        else:
            print("\033[43;1m您输入的选项有误，请重新输入！\033[0m")

def select():
    msg = '''
    *************查询方式***************
    1、select name,age from staff_table where age > 22
    2、select * from staff_table where dept = "IT"
    3、select * from staff_table where enroll_date like "2013"
    '''

    while True:
        print(msg)

def add():
    '''
    增加用户
    :return:
    '''
    while True:
        # ck_user = auth.check_user()  # 检测用户是否存在，如果存在返回用户已存在和信息
        curr_day = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username = input("用户名>>>:")
        phone = input("手机号>>>:")
        age = input("年龄>>>:")
        vocation = input("职业>>>:")
        company = input("公司名>>>:")

        add_info_dic = {
            'username':username,
            'phone':phone, # 11位
            'age':age,
            'vocation':vocation,
            'company':company,
            'enroll_day':curr_day
        }

        db_file = "%s/%s.json" %(db_path,phone)

        ck_user = auth.check_user(phone) # 检查用户是否存在，手机号唯一
        if ck_user: # 返回非空 手机号唯一判断 存在该手机号
            print("该用户手机号已经存在，请使用其他手机号！")
            print("按[b]返回上一层，或者按[q]退出程序")
            continue
        else:
            with open(db_file,'a+') as f:
                json.dump(add_info_dic,f)
                # return True

def update():
    '''
    用户信息修改，写回用户db文件
    :return:
    '''
    msg = u'''
    1、用户名
    2、手机号
    3、年龄
    4、职业
    5、公司名称
    '''
    msg_dic = {
    '1':'username',
    '2':'phone', # 11位
    '3':'age',
    '4':'vocation',
    '5':'company',
    '6':'enroll_day'
    }

    #提示输入手机号 (此处需要做位数（11位）限制
    user_phone = input("请输入您要修改的用户手机号>>>:")
    # 判断用户是否存在
    user_info = auth.check_user(user_phone)

    #用户数据更改流程
    if user_info: # Not None  返回了用户信息
        print(msg)  # 打印用户操作项
        # 提示用户输入项
        change_item = input("请选择您要修改的项目>>>:") # 3
        change_value = input("请输入您要修改的值>>>:")  # 输入不限制格式

        print("\033[42;1m%s\033[0m" % user_info)  # 打印用户信息

        # print(type(msg_dic[change_item]),msg_dic[change_item])
        # print(type(change_value),change_value)
        # print(type(user_info[msg_dic[change_item]]))
        user_info[msg_dic[change_item]] = change_value  # 给对应的要修改的key 复制 value

        #增加判断，如果修改的是手机号，需要把原手机号文件删除

        #将修改值写回文件
        db_file = "%s/%s.json" %(db_path,user_phone)
        with open(db_file,'w') as f:
            print(user_info)
            json.dump(user_info,f)
        return True

    else:
        print("您要修改的用户不存在")

def delete():
    pass


def log_out():
    print("\033[31;1mGoodBye!\033[0m".center(50,'-'))
    exit()

