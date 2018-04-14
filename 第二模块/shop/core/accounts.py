#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import json
import os
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from core import db_handler
from conf import settings

def dumpAccount(acc_data):
    '''
    序列化用户数据到文件
    :param acc_data:
    :return:
    '''
    account = acc_data['user']
    db_path = db_handler.db_handler(settings.DATABASE)
    acc_file = "%s/%s.json"%(db_path,account)
    # print("\033[42;1mdump:%s\033[0m"%acc_file)
    with open(acc_file,'w') as f:
        json.dump(acc_data,f)

def loadAccount(u_name):
    '''
    反序列化文件，显示用户数据
    :param acc_data:
    :return:
    '''
    account = acc_data['user']
    db_path = db_handler.db_handler(settings.DATABASE)
    acc_file = "%s/%s.json"%(db_path,account)
    # print("\033[42;1mdump:%s\033[0m"%acc_file)
    with open(acc_file) as f:
        acc_data = json.load(f)
        return acc_data



