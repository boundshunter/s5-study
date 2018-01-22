#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# import sys
# import os
# BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
# sys.path.append(BASE_DIR)
# from auth import acc_login
from core import logger
from core import auth

access_logger=logger.logger('access')

user_data = {
    'account_id':None,
    'is_authorized':False,
    'account_data':None
}

def get_user_data():
    account_data = auth.acc_login(user_data,access_logger)

    if user_data['is_authorized']:
        user_data['account_data'] = account_data
        return user_data
    else:
        return None

def manager_controll():
    '''

    :return:
    '''
    menu = u'''
    -----------管理员 选项------------
    1、添加用户
    2、查询用户信息
    3、修改用户信息（冻结账户，信用额度等）
    4、生成全部账单
    5、退出
    '''
    menu_dict = {
        '1':"auth.sign_up()",
        '2':"auth.account_info()",
        '3':"auth.account_modify()",
        '4':"get_all_bills()",
        '5':"exit_flag()"
    }
    go_flag = True
    while go_flag:
        print("\033[33;1m%s\033[0m]" % menu )
        user_choice = input(">>>>:")

        if user_choice in menu_dict:
            # print(menu_dict[user_choice])
            eval(menu_dict[user_choice])
            go_flag = False
        else:
            print("\033[31;1m您输入的选项有误，请重新输入\033[0m")
            continue


def exit_flag():
    print("----退出当前管理员[%s]----"%user_data['account_id'])
    exit()


def get_all_bills():
    pass

def login():
    print("Welcome to my homepage.")

# def run():
#     '''
#     程序开始会调用此方法用于和用户数据交互
#     :return:
#     '''
#     acc_data = auth.acc_login(user_data,access_logger)

def manager_run():
    print("\033[31;1m ATM管理员菜单 \033[0m".center(50,'#'))
    user_data = get_user_data()
    # print(user_data)
    manager_controll()


# manager_controll()