#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import datetime

# yesterday = datetime.datetime.now() + datetime.timedelta(days=-1)

# yesterday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
# # print("yesterday:",yesterday.strftime("%Y-%m-%d"))
# # print(int(yesterday.strftime("%Y")) + 3)
# print(type(yesterday.))
# print(expire_day)
account_data = {
    "enroll_date": "2018-01-21", "password": "abc", "id": "100", "credit": 15000,
    "status": 0, "balance": 0.0, "expire_date": "2021-01-20", "pay_day": 22
}
print(datetime.datetime.strptime(account_data['expire_date'],"%Y-%m-%d"))
