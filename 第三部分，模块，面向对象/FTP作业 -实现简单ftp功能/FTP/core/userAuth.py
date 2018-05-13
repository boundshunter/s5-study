#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'jfsu'

import sys
import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from conf import config

class users(object):
    def __init__(self):
        self.users_file = config.USERS_FILE+"user_db.txt"
        self.users = self.read_users()

    def read_users(self):
        print(self.users_file)
        with open(self.users_file,'r',encoding="utf-8") as f:
            users = eval(f.read())
            # print(users)
            return users

    def get_users(self):
        return self.users

    def get_user(self,username):
        for user in self.users:
            print("\033[42;1m>>>:\033[0m",user)
            if user['username'] == username:
                # print(user["password"])
                return user

# aa = users()
#
# aa.get_user('jfsu')