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
    amount = float(amount)
    if trans_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[trans_type]['interest']
        old_balance = account_data['balance']
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
        log_obj.info("accounts:%s   action:%s   amount:%s   interest:%s "
                     %(account_data['id'],trans_type,amount,interest))
        return account_data
    else:
        print("您的选项有误或不存在:%s"%(trans_type))
