#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

'''
记录所有日志，日志输出为屏幕输出和日志文件记录
'''
import logging
from conf import settings

def logger(log_type):

    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # 屏幕输出 screen output show
    screen_output = logging.StreamHandler()
    screen_output.setLevel(settings.LOG_LEVEL)

    # 日志文件输出 log file output
    log_file = "%slog%s"%(settings.BASE_DIR,settings.LOG_TYPES[log_type])
    log_file_output = logging.FileHandler()
    log_file_output.setLevel(settings.LOG_LEVEL)

    #日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

    screen_output.setFormatter(formatter)
    log_file_output.setFormatter(formatter)

    #屏幕输出和日志输出加入到logger
    logger.addHandler(screen_output)
    logger.addHandler(log_file_output)

    #返回输出
    return logger
