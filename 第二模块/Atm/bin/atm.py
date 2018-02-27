#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import sys

BASE_DIR = os.path.dirname( os.path.dirname( (os.path.abspath(__file__)) ) ) # 两次调用 parent 就返回了 home 目录
sys.path.append(BASE_DIR)
from core import main

if __name__ == '__main__':
    main.run()

