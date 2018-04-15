#!/usr/bin/env python3.6
#-*- coding:utf-8 -*-
# Author:summer_han

import paramiko
def connect(host):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
                ssh.connect(host,username='root',allow_agent=True,look_for_keys=True)
                #ssh.connect(host,username='hillstone',password='Abc,123.!',port="29999",allow_agent=True)
                ssh.connect(host,username='root',password='dongao.com123',allow_agent=True)
                return ssh
        except:
                return None



connect("172.16.0.141")