#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import json
import time
from core import db_handler
from conf import settings

def check_account(account,password):
    '''
    检测用户是否存在，检测用户和密码是否正确，用户存在返回用户数据，不存在则返回空
    :param account:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    acc_file = "%s/%s.json"%(db_path,account)
    # print(acc_file)
    if os.path.isfile(acc_file):
        with open(acc_file) as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                return account_data
            else:
                print("密码输入错误,程序退出")
                time.sleep(1)

    else:
        print("您输入的用户或密码错误，请重新输入")
        return None


