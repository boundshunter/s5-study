#!_*_coding:utf-8_*_
#__author__:"Alex Li"

import os
base_dir = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
file_dir = os.path.abspath(__file__)
print(file_dir)
import json
acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled, 8 = admin
}
# with open()
# print(json.dumps(acc_dic))
json.dumps(acc_dic)