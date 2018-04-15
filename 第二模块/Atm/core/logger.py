#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

'''
记录所有日志，日志输出为屏幕输出和日志文件记录
'''
import os,sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
import datetime
import logging
from conf import settings
from core import bill_date

def logger(log_type):
    '''
    日志输出和记录
    :param log_type:
    :return:
    '''
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # 屏幕输出 screen output show
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)  # 屏幕 输出 info

    # 日志文件输出 logs file output
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


def show_log(account,log_type,log_day):
    '''
    在操作日志中根据用户ID和账单时间匹配用户日志输出，用户名已转换成int,
    :param account: account_id
    :param log_type: logtype
    :param log_day: check_date (
    :return:
    '''
    year_month = log_day
    begin_time, end_time = bill_date.get_bill_time(year_month) # 通过 check_date 获取输入月份账单开始和结束时间

    log_file = "%s/logs/%s" % (settings.BASE_DIR, settings.LOG_TYPES[log_type]) # log_type = transaction
    file = open(log_file,'r')
    print(" account \033[32;1m[%s]\033[0m transaction ".center(60, "-")% account)
    for line in file:
        log_time = datetime.datetime.strptime(line.split(" - ")[0],"%Y-%m-%d %H:%M:%S")
        uid = line.split( )[7].split(":")[1]  # uid 默认 str 型，转换成 int
        u_name = int(uid)
        if log_time > begin_time and log_time < end_time and u_name == account:
            # print(type(account),log_type,log_day)
            print("\033[35;1m%s\033[0m" % line.strip( ))
    print("-".center(52, "-"))
    file.close()
