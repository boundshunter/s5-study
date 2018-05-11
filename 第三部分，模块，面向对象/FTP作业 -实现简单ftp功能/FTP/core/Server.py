#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import os
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from conf import config
class ftpServer:
    def __init__(self):
        self.server = config.socket.socket()
        self.bind(config.IP_PORT)
        self.listen(5)

    def start(self):
        while True:
