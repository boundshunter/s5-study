#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

from conf import settings
from core import accounts


def make_transaction(log_obj,account_data,trans_type,amount,**others):
    '''
    用户金额操作改动数据后存储日志，改动后返回用户数据
    :param log_obj:
    :param account_data:
    :param trans_type:
    :param amount:
    :param others:
    :return:account_data
    '''
    # 金额转换浮点类型
    amount = float(amount)

    #  判断 交易类型
    if trans_type in settings.TRANSACTION_TYPE:  # 交易类型存在
        interest = amount * settings.TRANSACTION_TYPE[trans_type]['interest']  # 定义利息
        old_balance = account_data['balance']   # 初始化 交易前的值

        #  根据交易类型，对金额进行加减操作，并减除带有利息的操作
        if settings.TRANSACTION_TYPE[trans_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
            account_data['balance'] = new_balance
            accounts.dump_account(account_data)

        elif settings.TRANSACTION_TYPE[trans_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print("\033[32;1m 您的信用额度为:[%s],您的额度不支持本次操作[-%s],您当前的余额为:[%s]\033[0m"
                      %(account_data['credit'],(amount +interest),old_balance))
                return False
            account_data['balance'] = new_balance
            accounts.dump_account(account_data)
        # log_obj = transaction_logger = logger.logger('transaction')
        # 将操作记录到日志文件
        log_obj.info("accounts:%s   action:%s   amount:%s   interest:%s "
                     %(account_data['id'],trans_type,amount,interest))
        return account_data
    else:
        print("您的选项有误或不存在:%s"%(trans_type))
