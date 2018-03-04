#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import logging
from conf import settings

def logger(log_type):

    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LOG_LEVEL)

    #屏幕打印
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)


    #日志记录到文件
    log_dir = "%s/%s" % (settings.LOG_DATABASE['path'],settings.LOG_DATABASE['type'])
    fh = logging.FileHandler(log_dir)
    fh.setLevel(settings.LOG_LEVEL)

    #设置日志格式
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

    ch.setFormatter(log_formatter)
    fh.setFormatter(log_formatter)

    #加入logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    #返回
    return logger

