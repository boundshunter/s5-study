#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import socket

client = socket.socket() # 声明socket 类型，同时建立链接对象
client.connect(('localhost',6868))

client.send(b'hello world')



data = client.recv(1024)

print(data)
client.close()
