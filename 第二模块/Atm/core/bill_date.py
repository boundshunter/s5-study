#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import sys
import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from conf import settings
import datetime


def get_bill_time(year_month):
    """
    获取给出的年-月的信用卡帐单月份起止时间
    :param year_month: 年-月
    :return: 返回日期
    """
    the_bill_day = "%s-%s" % (year_month, settings.BILL_DAY)  # 帐单日
    # print(the_bill_day)
    bill_begin_time = datetime.datetime.strptime(the_bill_day, "%Y-%m-%d")  # 给出的年-月帐单开始时间
    # print(bill_begin_time)
    year = bill_begin_time.year
    month = bill_begin_time.month
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
    bill_end_time = datetime.datetime(year, month, settings.BILL_DAY)
    # print(bill_end_time)
    return bill_begin_time, bill_end_time