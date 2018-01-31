#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

user_data = {'account_id': '100', 'is_authorized': True, 'account_data': {'enroll_date': '2018-01-21', 'password': 'abc', 'id': '100', 'credit': '20001', 'status': 0, 'balance': '1001', 'expire_date': '2021-01-20', 'pay_day': 22}}

print(user_data)

print(user_data['account_data']['status'])