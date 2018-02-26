#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# user_data = {'account_id': '100', 'is_authorized': True, 'account_data': {'enroll_date': '2018-01-21', 'password': 'abc', 'id': '100', 'credit': '20001', 'status': 0, 'balance': '1001', 'expire_date': '2021-01-20', 'pay_day': 22}}
#
# print(user_data)
#
# print(user_data['account_data']['status'])

# nb = 1001 -100.0 -5.0
# # print(nb)
# with open("C:\Users\sjf\PycharmProjects\s4\第二模块\Atm/logs/accounts/1001.bills",'r') as f:
#     bill_date = f.split(':')[0]
#     print(bill_date)

# import datetime
# i = datetime.datetime.now()
# # print(str(i).split( )[0])
# # print(i.strptime("%Y-%m"))
#
# exp_time_stamp = datetime.datetime.strftime(i,'%Y-%m')
# print(exp_time_stamp)

import datetime
with open("123",'r') as line:
    log_time = datetime.datetime.strptime("%Y-%m-%d %H:%M:%S")