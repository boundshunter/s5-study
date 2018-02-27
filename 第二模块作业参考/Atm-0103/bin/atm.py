#!/usr/bin/env python
#!_*_coding:utf-8_*_
#__author__:"Alex Li"

import os
import sys



base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
print(base_dir)

from core import main # 需要在 append（base_dir)之后才能调用

if __name__ == '__main__':
    main.run()
