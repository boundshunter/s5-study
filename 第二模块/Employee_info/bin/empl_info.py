#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import sys
import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

# 入口主函数
if __name__ == '__main__':
    main.run()