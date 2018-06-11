#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
import socket
import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)
from conf import config
import shelve

class FtpServer(object):
    def __init__(self):
        self.server = config.server
        self.server.bind(config.Ip_Port)
        self.server.listen(config.listen)
        self.clienthome = config.ClientHome
        self.userdb = {}
        self.fileobj = shelve.open(config.DB_Dir)
        self.manage()
        # self.fileobj.close()

    def start_server(self):
        while True:
            print("waiting connect....................")
            self.conn,self.addr = self.server.accept()
            print("-----connect established-----")
            while True:
                self.data = self.conn.recv(1024)
                # 判断连接如果为空，则重新等待连接
                if not self.data:break
                res = self.data.decode().split()
                action = res[0]
                if hasattr(self,action):
                    run = getattr(self,action)
                    run(res)
                else:
                    print("Command not found,Please input the correct again.")
    def ls(self, cmd):
        print("server recv info",cmd)
        if len(cmd) == 3:
            res = os.popen("%s %s %s"% (cmd[0], cmd[1], cmd[2])).read()
        elif len(cmd) == 2:
            res = os.popen("%s %s" % (cmd[0], cmd[1])).read()
        elif len(cmd) == 1:
            res = os.popen("%s" % cmd[0]).read()
        else:
            res = os.popen("%s" % cmd[0]).read()

        # 发送命令返回大小
        self.conn.send(len(res).encode())
        # 接收信号 ok
        ack = self.conn.recv(1024).decode
        if ack == "ok":
            self.conn.send(res.encode())

        self.conn.recv(1024).decode()
        print("server send result success:")

    def put(self, cmd):
        pass

    def get(self, cmd):
        pass

    def create_user(self):
        self.fileobj = shelve.open(config.DB_Dir)
        username = input("Input the username>>:").strip()
        password = input("Input the password>>:").strip()
        self.fileobj[username] = {'username':username,'password':password,'homedir':self.clienthome+username}
        print(self.fileobj[username])
        self.fileobj.close()

    def sel_user(self):
        '''
        查询用户
        :return:
        '''
        username = input("Input username>>:")
        for item in self.fileobj.items():
            # print('键[{}] = 值[{}]'.format(item[0], self.fileobj[item[0]]))
            if username in item[0]:
                dic = self.fileobj[item[0]]
                print("-----User Info-----\nuser:%s\npassword:%s\nhome:%s"%
                      (dic['username'],dic['password'],dic['homedir']))
    def manage(self):
        menu = '''
            \033[33;1m---------info---------
                1、创建用户
                2、查询用户
                3、开始程序\033[0m
                '''
        menu_dic = {
            '1': 'create_user',
            '2': 'sel_user',
            '3': 'start_server'
        }

        while True:
            print(menu)
            option = input("Input option>>:").strip()
            action = menu_dic[option]
            if hasattr(self, action):
                func = getattr(self, action)
                func()
            else:
                print("输入有误，请重新输入！")




