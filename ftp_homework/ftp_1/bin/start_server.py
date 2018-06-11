#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from core import ftpserver

if __name__ == '__main__':
    sv = ftpserver.FtpServer()
