#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': "%s/db/" % BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'shopping': 'shopping.logs',
    'access': 'access.logs',
}