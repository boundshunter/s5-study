#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# import os
# import sys
# BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

from conf import settings

# 数据引擎入口
def db_handler(conn_params):
    '''
    文件存储目录和路径
    :param conn_params:
    :return:
    '''
    #  返回用户存储目录
    db_path = "%s%s"% (conn_params['path'],conn_params['name'])
    return db_path
