#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import sys
import os

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

# 取金额参数
amount = sys.argv[1]

rlt = main.payApi(amount)

if rlt:
    exit(0)
else:
    exit(1)