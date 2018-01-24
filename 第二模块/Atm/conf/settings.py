#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}

LOG_DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/log" % BASE_DIR
}

LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}