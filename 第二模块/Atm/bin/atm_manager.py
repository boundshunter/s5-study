#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import sys

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)

from core import main

#  ATM 管理员入口
if __name__ == '__main__':
    main.manager_run()
