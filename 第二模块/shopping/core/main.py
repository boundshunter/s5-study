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

    # return True

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
        '2':"auth.sign_up()",
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
    interactive() # 登录，注册，退出
    account_data = user_data['account_data']
    user_name = user_data['user']

    log_type = "shopping"
    shopping_logger = logger.logger(log_type,username)
