#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

'''
记录所有日志，日志输出为屏幕输出和日志文件记录
'''
import os,sys

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)

import logging
from conf import settings

def logger(log_type):

    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # 屏幕输出 screen output show
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)  # 屏幕 输出 info

    # 日志文件输出 log file output
    log_file = "%s/logs/%s" % (settings.BASE_DIR,settings.LOG_TYPES[log_type])
    # print(log_file)
    fh = logging.FileHandler(log_file)

    fh.setLevel(settings.LOG_LEVEL)  # 日志记录 info

    #日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    #屏幕输出和日志输出加入到logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    #返回输出
    return logger


# logger('transaction').info("123")