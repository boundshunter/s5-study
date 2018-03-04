#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han



def file_handler(conn_parms):
    db_path = "%s%s" %(conn_parms['path'],conn_parms['name'])
    return db_path


def db_handler(conn_parms):
    if conn_parms['engine'] == 'file_storage':
        return file_handler(conn_parms)