#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
#实现简单 sed 替换功能
#查
#新建
#删除
#修改

arg= {
    'backend':'www.oldboy.org',
    'record':{
        'server':'100.1.7.9',
        'weight':20,
        'maxconn':3000
    }

}
print(arg)
#字符串转换字典
'''
b = {
    'backend':'www.oldboy.org',
    'record':{
        'server':'100.1.7.9',
        'weight':20,
        'maxconn':3000
    }

}'''

#删除
b = '''{
    'backend':'www.oldboy.org',
    'record':{
        'server':'100.1.7.9',
        'weight':20,
        'maxconn':3000
    }

}'''
b=eval(b) #字符串转换成字典

print(b['record'])



