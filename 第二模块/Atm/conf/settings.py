#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
BILL_DAY = 25
DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}

LOG_DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/logs" % BASE_DIR
}

LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'transaction': 'transactions.logs',
    'access': 'access.logs',
}

TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0}, # 还款
    'receive': {'action': 'plus', 'interest': 0},   # 接收
    'withdraw': {'action': 'minus', 'interest': 0.05},  # 提款
    'transfer': {'action': 'minus', 'interest': 0.05},  # 转出
    'pay': {'action': 'minus', 'interest': 0},  # 支付
    'save': {'action': 'plus', 'interest': 0},  # 存钱

}