#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import socket
import os

server = socket.socket()
server.bind(('127.0.0.1',8888))
server.listen(5)

while True:
    print("\033[35;1m开始等待\033[0m")
    conn,addr = server.accept() # 等待接收
    print("\033[33;1m数据进入:\033[0m%s"%conn)
    while True:
        data = conn.recv(1024)
        server.send(data)
server.close()

