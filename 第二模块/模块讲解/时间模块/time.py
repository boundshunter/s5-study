#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import time
import datetime
# print(time.localtime())

# print(time.timezone)

print(datetime.datetime.now())

print(time.time()) # 时间戳
print(datetime.date.fromtimestamp(time.time()))
# print(datetime. + datetime.timedelta(3)
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间 +3天
print(datetime.datetime.now() + datetime.timedelta(-3)) # 当前时间 -3天

print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时

print(datetime.datetime.now() + datetime.timedelta(minutes=-30))  # 当前时间 -30 分钟


# print(datetime.timedelta(years=3))

c_time = datetime.datetime.now()
print(c_time.replace(minute=15,hour=12,year=2015)) #当前时间 分钟数替换成 15,小时替换成 12,年份 替换成 2015

print((datetime.datetime.now() +datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))

abc = (int(datetime.datetime.now().strftime('%Y')) + 3)

# print((datetime.datetime.now().strftime('%Y-%m-%d').replace(int(datetime.datetime.now().strftime('%Y'))+3) + datetime.timedelta(days=-1))

# print(datetime.datetime.now().strftime('%Y-%m-%d').replace(int(datetime.datetime.now().strftime('%Y'))+3))
print(datetime.datetime.now().strftime('%Y-%m-%d'))


a = datetime.datetime.now().strftime("%Y-%m-%d") + datetime.timedelta(days=-1)

print("aaa:",a)
# print("bbb:",b)