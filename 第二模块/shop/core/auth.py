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

    #  根据用户获取数据文件存储路径
    db_path = db_handler.db_handler(settings.DATABASE)
    acc_file = "%s/%s.json"%(db_path,account)

    # 判断文件是否存在（用户是否存在），存在则打开文件，加载数据，返回用户数据
    if os.path.isfile(acc_file):
        with open(acc_file) as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                return account_data
            else:
                print("密码输入错误,程序退出")
                time.sleep(1)

    else: # 否则提示错误信息
        print("您输入的用户或密码错误，请重新输入")
        return None


