#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

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
    print("get_user_data:",account_data)
    if user_data['is_authorized']:
        user_data['account_data'] = account_data
        print(user_data)
        return user_data
    else:
        return None




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