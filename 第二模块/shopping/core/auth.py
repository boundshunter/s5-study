#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import json
import datetime
from core import db_handler
from conf import settings
from core import accounts

def acc_auth(account,password):
    '''
    认证成功返回用户数据
    :param account:
    :param password:
    :return: account_data eg:{'enroll_date': '2018-04-09 16:41:09', 'user': 'tech', 'password': 'tech', 'status': 0, 'balance': 50000.0}
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account)

    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                # print("acc_data:",account_data)

                return account_data
            else:
                print("\033[32;1m您的密码有误,请重新输入\033[0m")
    else:
        print(account_file)
        print("\033[32;1m您的用户不存在,请先注册用户!\033[0m")
        # return True

def check_account(account):
    '''
    检测用户是否存在
    :param account:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account)
    # print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
        return account_data

    else:
        return None

def sign_up(user_data):
    '''
    用户注册，判断用户是否存在，不存在则注册
    :return:
    '''
    curr_day = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    exit_flag = True
    while exit_flag is True:
        account = input("请输入用户名>>>:".strip())
        password = input("请输入密码>>>:".strip())
        user_exist = check_account(account) # return account_data
        if user_exist is not None: # 非空
            print("\033[42;1m 用户[%s]已存在，请使用其他用户重新注册\033[0m".center(20,'*') % account)

        else:
            account_data = {
                'enroll_date': curr_day,
                'user': account,
                'password': password,
                'status': 0,
                'balance': 50000.0,
             }
            accounts.dump_account(account_data)

            print("\033[35;1m 您的用户注册成功！\033[0m".center(50,'-'))
            user_info = '''
            用户信息：
            用户:%s
            密码:%s
            余额:%s
            '''%(account_data['user'],account_data['password'],account_data['balance'])
            print("%s" % user_info )
            user_data['is_authorized'] = True
            user_data['user'] = account
            user_data['account_data'] = account_data
            print("user_data:",user_data)


        return True
