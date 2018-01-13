#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

from auth import acc_login
from core import logger
access_logger=logger.logger()

def login():
    print("Welcome to my homepage.")

def run():
    '''
    程序开始会调用此方法用于和用户数据交互
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)