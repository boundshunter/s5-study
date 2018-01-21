#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import pickle
data={'k1':123,'k2':'hello'}

# p_str = pickle.dumps(data)
# print("pickle:",p_str)
#
# with open ('D:/result.pk','w',encoding="utf-8") as fp:
#     pickle.dump(data,fp)

import json
j_str = json.dumps(data)
print("json:",j_str)

with open('D:/result.json','w') as fp:
    json.dump(data,fp)
