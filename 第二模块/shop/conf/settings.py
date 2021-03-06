#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import os

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': "%s/db/" % BASE_DIR
}

LOG_TYPES = {
    'shopping': 'shopping.log',
    'access': 'access.log',
}