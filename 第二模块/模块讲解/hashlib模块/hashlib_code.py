#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
# 原则 SHA比 md5 更安全

import hashlib

m = hashlib.md5()
m.update(b'Hello')
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest()) # 加密的是 Hello it's me
# m.update(b"it's me a logs time")
# print(m.hexdigest())

m2=hashlib.md5()
m2.update(b"HelloIt's me")
print(m2.hexdigest()) # 此段输出结果等同 上面输出

s2 = hashlib.sha1()
s2.update(b"HelloIt's me")
print(s2.hexdigest())

#  hexdigest() 16进制
s3 = hashlib.sha256()
s3.update("HelloIt's me天大".encode(encoding="utf-8")) # 有中文需要encode
print(s3.hexdigest())

# 还有一种 hmac 消息加密，速度快
import hmac

h = hmac.new(b"33256","传入消息".encode(encoding="utf-8"))
print(h.digest())
print(h.hexdigest())

