#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import os
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from conf import config
from core import UserAuth

class ftpServer:
    def __init__(self):
        self.server = config.socket.socket()
        self.server.bind(config.IP_PORT)
        self.server.listen(5)
        self.userobj = UserAuth.users() # 把users类实例化
        self.start()

    def start(self):
        while True:
            print("服务器正在等待连接...")
            self.conn,self.addr = self.server.accept()
            print("一个连接建立",self.conn)
            while True:
                self.data = self.conn.recv(1024)
                if not self.data: # 判断接收为空
                    print("客户端断开连接")
                    break
                # 数据不为空，继续执行
                res = self.data.decode().split() # py3 中每一步都接收和发送都需要转码
                action = res[0] # 接收执行动作

                if hasattr(self,action): # 反射
                    foo = getattr(self,action) # 存在获取执行动作
                    foo(res) # 少解释***************************************************************
                else:
                    print("输入错误")

    def auth(self,cmd):
        print(cmd) # cmd 格式 auth username password
        user = self.userobj.get_user(cmd[1]) # 从获取用户名中去 userauth中做认证，userauth，认证成功返回user的字典
        print(user)
        if user: # 判断用户字典非空
            if user['password'] == cmd[2]: # 判断密码是否正确
                self.curr_user = user
                self.curr_path = user['home']
                self.user_home = config.USER_HOME
                self.conn.send(b'ok')
            else:
                self.conn.send(b'password is wrong')
        else:
            self.conn.send(b'%s is not exist'%cmd[1])


