#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import json
acc_dic = {
    'id': 'abc',
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled, 8 = admin
}

print(json.dumps(acc_dic))
