#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import socket
server = socket.socket()
server.bind(('127.0.0.1',6868))
server.listen()

print("开始等待接收")
conn,addr = server.accept() # 等待连接请求
print(conn,'\033[42;1m分隔符\033[0m',addr)
print("接收内容")

data = conn.recv(1024)
print('server recv:',data)
conn.send(data.upper())
