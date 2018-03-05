#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import logging

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'db',
    'path': "%s/" % BASE_DIR
}

LOG_DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/logs" % BASE_DIR,
    'type':"transactions.logs"
}

LOG_LEVEL = logging.INFO

# LOG_TYPES = {
#     'transaction': 'transactions.logs'
# }