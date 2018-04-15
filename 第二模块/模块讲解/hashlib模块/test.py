#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import hashlib

md5 = hashlib.md5()
md5.update(b'123')
print(md5.hexdigest())

def get_md5(password):
    # 获取 md5
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

get_md5('passwd'.encode('utf-8'))