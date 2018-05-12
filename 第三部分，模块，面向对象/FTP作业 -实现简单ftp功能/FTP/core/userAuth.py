#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys
import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from conf import config

class users:
    def __init__(self):
        self.users_file = config.USERS_FILE
        self.users = self.read_users()

    def read_users(self):
        with open(self.users_file,'r') as f:
            print(self.users_file)
            users = eval(f.read())
        return users

    def get_users(self):
        print(self.users)
        return self.users

    def get_user(self,username):
        for user in self.users:
            print(user)
            if user['username'] == username:
                return user

    # def user_regist(self,username):

