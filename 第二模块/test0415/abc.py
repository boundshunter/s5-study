#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import sys
import os

base=os.path.dirname(os.path.abspath(__file__))
print(base)
sys.path.append(base)

from aaa import run

run.comm()

