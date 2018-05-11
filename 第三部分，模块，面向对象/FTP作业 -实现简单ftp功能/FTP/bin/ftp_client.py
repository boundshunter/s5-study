#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys
import os

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)

from core import Client

if __name__ == '__main__':
    fc = Client.ftpClient()