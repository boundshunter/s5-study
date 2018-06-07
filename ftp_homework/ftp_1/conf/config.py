#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)
import socket

# server socket
server = socket.socket()

# ip_port
Ip_Port = ('127.0.0.1', 9000)

# 监听
listen = 5

# client socket
client = socket.socket()

# server home
ServerHome = BaseDir + '/db/server/'

# client home
ClientHome = BaseDir + '/db/home/'

# db directory
DB_Dir = BaseDir + '/db/' + 'fdb'
