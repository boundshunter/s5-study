#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

from conf import settings

def db_handler(conn_params):
    '''
    返回用户数据存储路径，从配置文件读出，conn_params 为配置文件中 字典
    :param conn_params:
    :return:
    '''
    db_path = "%s%s" % (conn_params['path'],conn_params['name'])
    return db_path


def file_handler(conn_params):
    '''
    通用函数
    判断，根据不同存储类型返回值，暂时只有一种文件存储类型
    :param conn_params:
    :return: db_path
    '''
    if conn_params['engine'] == 'file_storage':
        return file_handler(conn_params)
