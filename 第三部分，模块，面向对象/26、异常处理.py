#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

#1、
a = ['name','age']
d = {}
try:
    a[3]
    d['name']
except (IndexError,KeyError) as e:
    print("xxx",e)

#这种情况下，实际是2个错误，但是当捕获到第一个错误后，后面就不显示了
# 此种情况适用于，当多种错误只需要同一种输出提示时使用


#2、
# 万能异常
try:
    d['name']
    a[3]
except Exception as e : #不建议使用
    print("kkk",e)

# 3
try:
    # d['name']
    open('aaa.txt')
    # a[0]
except (KeyError,IndexError) as e:
    print("没有这个key",e)

except IndexError as e:
    print("列表操作错误",e)
except Exception as e:
    print("未知错误",e)

else: # 没出错的时候 到这
    print("没出错，一切正常")

finally:
    print("不管有没有错，都会执行")

# 缩进错误，语法错误是抓不到的

#自定义异常
class JfsuError(Exception):
    def __init__(self,msg):
        self.message = msg

#触发自定义异常
try:
    raise JfsuError("Jfsu 连接异常") # 触发异常，raise（触发）
except JfsuError as e:
    print(e)

