#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
# import os,sys
# sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) )))

# from conf import settings

def file_handler(conn_parms):
    db_path = '%s/%s'%(conn_parms['path'],conn_parms['name'])
    return db_path



def db_handler(conn_parms):   # conn_parms = settings.DATABASE 字典
    if conn_parms['engine'] == 'file_storage':
        return file_handler(conn_parms)

# db_handler(settings.DATABASE)

