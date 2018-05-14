#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys
import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config
from core import UserAuth

class ftpClient:
    def __init__(self):
        self.client = config.socket.socket()
        self.client.connect(config.IP_PORT)
        self.help = {
            "get":"用于下载，如: get abc.txt,即 get 文件名",
            "put":"用于上传，如: put abc.txt,即 put 文件名",
            "ls":"用于显示当前目录下的文件列表详细信息",
        }
        if self.auth(): # 做用户认证，判断用户是否有权限登录
            self.start()

    def auth(self):
        username = input("\033[35;1mftp账户>>:\033[0m".strip())
        password = input("\033[35;1mftp密码>>:\033[0m".strip())
        auth_info = "auth %s %s"% (username,password)
        self.client.send(auth_info.encode()) # py3 发送和接收都需要转码，每次发送encode，接收decode
        bak_res = self.client.recv(1024).decode()

        if bak_res == "ok":
            print("您的用户登录成功...")
            self.curr_user = username
            self.curr_password = password
            self.curr_dir = bak_res[1] # server端发送结果，bak_res[0] 为认证状态，bak_res[1] 为认证成功返回目录
            return True
        else:
            print("用户名或密码有误,请重新输入")

    def start(self):
        while True:
            user_input = input("%s>>:"% self.curr_user.strip()) # 获取命令
            if len(user_input) == 0:
                continue
            user_input = user_input.split()
            if user_input[0] == 'q':
                break
            if hasattr(self,user_input[0]):
                func = getattr(self,user_input[0])
                func(user_input)
            else:
                print("command not found,please input again.")
                continue

    def put(self,cmd):
        print(cmd)
        put_file_name = cmd[1]
        # 判断文件是否存在
        if os.path.isfile(put_file_name):
            # 获取上传文件大小
            total_size = os.stat(put_file_name).st_size
            # 上传文件 状态信息 发送到 server 端 例: put 文件名 文件大小（size)
            send_info = "%s %s %s"%(cmd[0],put_file_name,total_size)
            # 发送信息到server端,并且进行转码 py3中需要每次转码
            self.client.send(send_info.encode())
            # 设定每次接收文件大小，并进行转码
            server_back = self.client.recv(1024).decode()
            if server_back == "200": # 握手成功
                print("上传开始.......")
                # 初始化上传大小为0
                send_file_size = 0
                with open(put_file_name,'r') as f:
                    # 发送大小 不等于 总大小，就一直执行循环
                    while send_file_size != total_size:
                        # 如果总大小 - 已发送大小 小于等于 1024，说明一次剩下的一次可以发送完毕
                        if total_size - send_file_size <= 1024:
                            data = f.read(total_size-send_file_size)
                            send_file_size = total_size
                        else:
                            data = f.read(1024)
                            send_file_size += len(data)
                        self.client.send(data.encode())
                print("Upload success complete.")
        else:
            print("The upload file not found")

    def ls(self,cmd):
        print(cmd[0])
        client_send_to_server_info = "%s"% cmd[0]
        self.client.send(client_send_to_server_info.encode())
        server_back = self.client.recv(1024).decode()
        print("server back result:\n",server_back) # 返回命令结果的大小
        self.client.send("ok".encode()) # 发送ok 确定可以收了
        recv_size = 0
        recv_data = b""
        while recv_size < int(server_back):
            data = self.client.recv(1024)
            recv_data = data
            recv_size += len(data)
            print(recv_size)
        else:
            print(recv_data.decode())

    def help(self,cmd):
        if len(cmd) == 1:
            for k,v in self.help.items():
                print("%s : %s"% (k,v))


