#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import logging

# 日志输出到文件中
# logging.basicConfig(filename="logging.log",level=logging.DEBUG,format='%(asctime)s %(message)s ',datefmt='%Y-%m-%d %H:%M:%S')
# level (DEBUG,INFO,WARNING,ERROR,CRITICAL)
# logging.basicConfig(filename="log1.log",level=logging.INFO,format='%(asctime)s %(levelname)s  %(filename)s %(message)s',datefmt='%Y-%m-%d %I:%M:%S')
# 时间格式 自定义
# 固定时间格式
# 时间和日志空格分隔
# format='%(asctime)s%(levelno)s%(message)s ',datefmt='%Y-%m-%d %H:%M:%S '
#datefmt 最后的 空格  用于 分隔 系统时间和 日志输出，不加 空格就都连在一起了。


# 日志输出

# logging.debug("123")
# logging.info("456")
# logging.warning("User [苏俊峰] attempt wrong password 3 times".encode(encoding="utf-8"))
# logging.error("error msg")
# logging.critical("server is down")

# 默认值打印warning级别日志


# 文件和屏幕同时输出


# import logging

#create logger
logger = logging.getLogger('test-log')
logger.setLevel(logging.DEBUG)

# 创建屏幕输出，定义 日志输出 级别
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # debug 级别以下都输出到屏幕

# 创建文件输出，定义 日志输出 级别
fh = logging.FileHandler("access.log",encoding="utf-8") # 写入文件日志支持中文
fh.setLevel(logging.ERROR)  # 只记录 error 和更严重级别 到日志

# 建立 formatter
ch_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
fh_formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

# formatter 加入到 ch 和 fh
ch.setFormatter(ch_formatter)
fh.setFormatter(fh_formatter)

# 把ch 和 fh加入 到logger
logger.addHandler(ch)
logger.addHandler(fh)

# app code
logger.debug("test debug")
logger.info("test info")
logger.warning("test warning")
logger.error("test error")
logger.critical("test critical")




