#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import logging
from conf import settings

def logger(log_type):

    #设置logger 和 日志级别
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    #屏幕输出
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    #定义日志记录路径
    log_file = "%s/logs/%s" % (settings.BASE_DIR,settings.LOG_TYPES[log_type])
    #日志记录
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    #日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)')

    #定义 ch  fh 日志格式
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    #把屏幕输出 和日志记录 加入到 logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    # 返回
    return logger

