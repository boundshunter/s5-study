#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import subprocess

p=subprocess.Popen("echo 'aaa' | sudo -S yum -y install vim",shell=True,stdout=subprocess.PIPE)

