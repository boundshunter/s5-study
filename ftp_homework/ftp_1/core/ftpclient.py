#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import socket
import shelve
import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)
from conf import config


class FtpClient(object):
    def __init__(self):
        self.client = config.client
        self.client.connect(config.Ip_Port)
        self.fileobj = shelve.open(config.DB_Dir)
        self.auth()

    def auth(self):
        username = input("Input username>>:").strip()
        password = input("Input password>>:").strip()
        for item in self.fileobj.items():
            # print('键[{}] = 值[{}]'.format(item[0], self.fileobj[item[0]]))
            if username in item[0]:
                dic = self.fileobj[item[0]]
                # print("-----User Info-----\nuser:%s\npassword:%s\nhome:%s"%
                #       (dic['username'],dic['password'],dic['homedir']))
                if dic['password'] == password:
                    print("Welcome %s,Login success."% username)
                    self.client_start()
                else:
                    print("Your password is incorrect")
            else:
                print("Your name %s is incorrect"% username)

    def client_start(self):
        while True:
            user_input = input(">>:").strip()
            if not user_input:
                continue

            user_input = user_input.split()
            if user_input[0] == 'q':
                sys.exit("Program Exit.")

            action = user_input[0]
            if hasattr(self, action):
                func = getattr(self, action)
                func(user_input)
            else:
                print("Command not found,try anthor again.")
                continue
    def ls(self, cmd):
        if len(cmd) == 3:
            send_cmd = "%s %s %s"% (cmd[0], cmd[1], cmd[2])
        elif len(cmd) == 2:
            send_cmd = "%s %s"% (cmd[0], cmd[1])
        else:
            send_cmd = "%s"% cmd[0]
        self.client.send(send_cmd.encode())
        # 接收命令大小
        sv_back_size = self.client.recv(1024).decode()
        print("接收命令大小",sv_back_size)
        # 发送准备信号
        self.client.send("ok".encode())
        # 循环接收结果
        recv_res = 0
        while recv_res < sv_back_size:
            data = self.client.recv(1024).decode()
            recv_res += len(data)

        print("client recevice server back complete.")

    def put(self, cmd):
        pass

    def get(self, cmd):
        pass
