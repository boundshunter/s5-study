#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import os
import sys

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import auth
from core import logger


# access logger
access_logger = logger.logger('access')

# 初始化用户临时数据
user_data = {
    'is_authorized':False,
    'account_data':None
}


def user_login():

    print("\033[33;1m 欢迎光临 \033[0m".center(50,'-'))
    account = input("\033[35;1m请输入用户>>>：\033[0m".strip())
    password = input("\033[35;1m请输入密码>>>:\033[0m".strip())
    acc_data = auth.acc_auth(account,password)
    return acc_data
    # acc_data = auth.acc_auth(account,password)
    # print("acc_data_user_login:",acc_data)
    # return acc_data

def user_exit():
    print("\033[35;1m Welcome back again,Goodbye! \033[0m".center(30,'-'))
    exit()

def interactive():
    menu = u'''
    ----------- 用户选项 -----------
    1、登录
    2、注册
    3、退出
    '''
    menu_dict = {
        '1':"user_login()",
        '2':"auth.sign_up(user_data)",
        '3':"user_exit()"
    }

    go_flag = True
    while go_flag:
        print("\033[31;1m %s \033[0m" % menu )
        user_choice = input("您的选项>>>:".strip())

        if user_choice in menu_dict:
            go_flag = eval(menu_dict[user_choice])

        else:
            print("\033[35;1m您输入的选项有误，请重新输入\033[0m")
            continue



def run():
    print("\033[35;1m welcome to Shopping Mall \033[0m".center(70,'-'))
    rlt=interactive() # 登录，注册，退出
    print("rlt",rlt)
    #return acc_data_user_login: {'enroll_date': '2018-03-03 12:22:31', 'user': 'test', 'password': 'test', 'status': 0, 'balance': 50000.0}
    # account_data = get_user_data()
    # print("111111111111",account_data)

