#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os

import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
import json
import datetime

# db_dir = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
# sys.path.append(db_dir)
#
from core import db_handler
from conf import settings


def acc_auth(account,password):
    db_path = db_handler.db_handler(settings.DATABASE)  # settings.DATABASE = conn_parms
    account_file = "%s/%s.json" % (db_path, account)
    # print(db_path)
    # print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            # print(account_data)

        if account_data['password'] == password:

            exp_time_stamp = datetime.datetime.strptime(account_data['expire_date'],'%Y-%m-%d')
            '''
            注意 strptime 和 strftime的区别
            strftime 是日期转换成字符串 datetime.datetime.now().strftime('%b-%d-%y %H:%M:%S')
            strptime 是字符串转换成日期 datetime.datetime.strptime('sep-21-09 16:33:33','%b-%d-%y %H:%M:%S')

           '''
            status = account_data['status']
            if datetime.datetime.now() > exp_time_stamp:
                print("\033[32;1m您的账户 [%s] 已过期，请联系管理员申请新的卡片！\033[0m"%(account))
            elif status == 0  or status == 8:
                # print(account_data)
                return account_data
            else:
                print("\033[31;1m您的账户状态有误，请联系管理员\033[0m")
        else:
            print("\033[32;1mAccount or password is not incorrect\033[0m")
    else:
        print(" 您的账户\033[33;1m [%s] \033[0m不存在"%(account))





def acc_login(user_data,log_obj):
    account = input('请输入账户ID:'.strip())
    password = input('请输入密码:'.strip())

    retry_count = 0
    exit_count = 3
    same_count = 0

    while user_data['is_authorized'] is False and retry_count < exit_count:
        auth = acc_auth(account,password)  # 返回 account_data  登录验证：验证用户，密码，状态，是否过期

        if auth:  # 如果非空
            user_data['is_authorized'] = True
            user_data['account_id'] = account

            return auth

        retry_count += 1

    else:
        same_count += 1
        if same_count == 3:
            log_obj.error("accounts [%s] too many login attempts" % account)
            exit()



def sign_up(account,password):
    # account =
    # password =
    enroll_day =
    print(enroll_day)
    data_exp = {'enroll_date': enroll_day,
                'password': account,
                'id': password,
                'credit': 15000,
                'status': 8,
                'balance': 0.0,
                'expire_date': '3000-01-01',
                'pay_day': 0
}

def account_info():
    pass

def account_modify():
    pass

sign_up('abc','abc')