#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
'''
#server端
import socket
socket.TCP/IP

listen(0.0.0.0:port)
waiting()
recv()
send

#client端
import socket
socket.TCP/IP
connect(a,ip,a.port)
socket.send(hello)
socket.recv
socket.close()
http://www.cnblogs.com/alex3714/articles/5830365.html
'''

# client 端
import socket
import os

client = socket.socket()# 声明socket 类型，同时生成socket连接对象
client.connect(('localhost',6969))

while True:
    # client.send(b"Hello,World!") # 默认bytes 类型，如果想写中文
    msg = input(">>:")
    client.send(msg.encode("utf-8"))
    data = client.recv(102400) # 1024个字节 ，1k
    print("recv:",data.decode()) # 由于上面中文被转换成asicii，转换成中文识别，需要再次decode

# # server 端
# import socket
# server = socket.socket()  # 声明类型，生成连接对象
# server.bind(('localhost',6969)) # 绑定server 监听端口
# server.listen() # 监听端口，先绑定后监听
#
# print("starting wait...")
# conn 就是客户端连接过来，而服务器端为其生成的一个连接实例
# conn,addr = server.accept() # 等待 请求
#
# print("new conn incoming")
# data = conn.recv(1024) # 接收数据大小 1024字节
# print("recv:",data)
# conn.send(data.upper()) # 发送大写的返回数据
#
# server.close() # 关闭连接



