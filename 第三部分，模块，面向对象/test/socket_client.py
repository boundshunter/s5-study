#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import socket
client = socket.socket()
client.connect(('127.0.0.1',8888))

while True:
    msg = input(">>:".strip())
    if len(msg) == 0: continue
    client.send(msg.encode("utf-8"))
    client.recv(10240)

client.close()