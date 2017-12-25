#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import configparser # 2.x  ConfigParser

# # 先生成文件
#
# config = configparser.ConfigParser()
#
# #         key                     value
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'     # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#    config.write(configfile)


>>> import configparser
>>> config = configparser.ConfigParser()
>>> config.sections()
[]
>>> config.read('example.ini')
['example.ini']
>>> config.sections()
['bitbucket.org', 'topsecret.server.com']
>>> 'bitbucket.org' in config
True
>>> 'bytebong.com' in config
False
>>> config['bitbucket.org']['User']
'hg'
>>> config['DEFAULT']['Compression']
'yes'
>>> topsecret = config['topsecret.server.com']
>>> topsecret['ForwardX11']
'no'
>>> topsecret['Port']
'50022'
>>> for key in config['bitbucket.org']: print(key)
...
user
compressionlevel
serveraliveinterval
compression
forwardx11
>>> config['bitbucket.org']['ForwardX11']
'yes'

# 读取文件

conf = configparser.ConfigParser()
conf.read('example.ini')

# for i in conf.defaults():
#     print(i)

print(conf.defaults())
print(conf['bitbucket.org']['user'])

sec = conf.remove_section('bitbucket.org') # 删除bitbucket.org
conf.write(open('example.cfg','w'))  # 写入新文件



[section1]
k1 = v1
k2:v2

[section2]
k1 = v1

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('i.cfg')

# ########## 读 ##########
#secs = config.sections()
#print secs
#options = config.options('group2')
#print options

#item_list = config.items('group2')
#print item_list

#val = config.get('group1','key')
#val = config.getint('group1','key')

# ########## 改写 ##########
#sec = config.remove_section('group1')
#config.write(open('i.cfg', "w"))

#sec = config.has_section('wupeiqi')
#sec = config.add_section('wupeiqi')
#config.write(open('i.cfg', "w"))


#config.set('group2','k1',11111)
#config.write(open('i.cfg', "w"))

#config.remove_option('group2','age')
#config.write(open('i.cfg', "w"))