#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

info = {
    'name':'jfsu',
    'age':20
}

import pickle

# with open("test2.txt",'wb') as f:
#
#     pickle.dump(info,f) # 完全等同于 f.write(pickle.dumps(info))


with open('test2.txt','rb') as f:
    a = pickle.load(f)  #反序列化也完全等同于.loads(f.read())
    print(a['age'])


写程序，永远 只dump一次，只load一次，不要多次dump和多次load