#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import datetime
import json
import glob

from core import db_handler
from core import auth
from conf import settings
from core import logger

# 用户存储在同一个db file 全局路径设置
db_path = db_handler.db_handler(settings.DATABASE)
# 定义日志级别
transaction_logger = logger.logger('INFO')

def run():

    msg = u'''
    \033[32;1m------------操作选项----------
    1、查询用户信息
    2、增加用户
    3、修改用户信息
    4、删除用户
    5、退出
    \033[0m
        '''

    msg_dic = {
        '1':"select()",
        '2':"add()",
        '3':"update()",
        '4':"delete()",
        '5':"log_out()"
    }
    go_flag = True
    while go_flag:
        print(msg)
        user_choice = input("\033[35;1m请输入您的选择>>>:\033[0m")

        if user_choice in msg_dic:
            go_flag = eval(msg_dic[user_choice])

        else:
            print("\033[43;1m您输入的选项有误，请重新输入！\033[0m")

def select():
    '''
    根据不同查询条件显示查询结果，并且在结果下面显示查询到匹配条件的数目
    :return:
    '''
    msg = '''\033[31;1m
    ************************** 查询类型 ***********************
    1、select name,age from staff_table where age > 22
    2、select * from staff_table where dept = "IT"
    3、select * from staff_table where enroll_date like "2013"
    ***********************************************************
    \033[0m'''

    # 定义选择 操作 类型 字典
    msg_dic = {
        '1':"select name,age from staff_table where age > []  (eg:22) >>:",
        '2':"select * from staff_table where dept = [])  (eg:IT)>>:",
        '3':"select * from staff_table where enroll_date like [] (eg:2013) >>:"
    }

    while True:
        print(msg)
        num = input("请输入查询类型编号：")
        count = 0 # 初始化 次数统计
        os.chdir(db_path)
        if num in msg_dic: # 判断输入编号是否存在
            term = input("请输入[]内您的条件:%s".strip() % msg_dic[num])
            if num == '1':  # 判断第一个条件 age 的输出结果
                # count = 0
                for file in glob.glob("*.json"):
                    with open(file,'r',encoding='utf8') as f:
                        term_db = json.load(f)   # 把所有文件结果循环输出

                    term_age = int(term_db['age'])   # 获取文件中的条件
                    term = int(term)

                    if term_age > term:  # 判断条件
                        count += 1
                        temp1_msg = '''
                        -------------查询结果-----------
                        用户名:%s
                        年龄:%s
                        '''% (term_db['username'],term_db['age'] )
                        print(temp1_msg) # 打印符合条件的结果
                print("%s result has been found!"%count) # 打印匹配结果个数

            if num == '2':
                # count = 0
                for file in glob.glob("*.json"):
                    with open(file,'r',encoding='utf8') as f:
                        term2_db = json.load(f)  # 加载所有文件数据

                    term_dept = term2_db['vocation']  # 获取部门

                    if term_dept == term: # 判断部门是否符合条件
                        count += 1
                        temp2_msg = '''
                        -------------查询结果-----------
                        用户名:%s
                        电话:%s
                        年龄:%s
                        部门:%s
                        公司:%s
                        注册日期:%s
                        '''\
                                    % ( term2_db['username'],term2_db['phone'],term2_db['age'],term2_db['vocation'],term2_db['company'],term2_db['enroll_day'] )
                        print(temp2_msg)  # 将符合条件的结果打印
                print("%s results has been found!"%count) # 打印匹配结果个数

            if num == '3':

                for file in glob.glob("*.json"):
                    with open(file,'r',encoding='utf8') as f:
                        term3_db = json.load(f)

                    term_date = term3_db['enroll_day'].split()[0].split('-')[0]  # 获取条件中日期项，取日期年-月-日
                    # print(type(term_date),term_date,type(term),term)
                    if term_date == term: # 判断符合条件日期
                        count += 1
                        temp3_msg = '''
                        -------------查询结果-----------
                        用户名:%s
                        电话:%s
                        年龄:%s
                        部门:%s
                        公司:%s
                        注册日期:%s
                        '''\
                                    % ( term3_db['username'],term3_db['phone'],term3_db['age'],term3_db['vocation'],term3_db['company'],term3_db['enroll_day'] )
                        print(temp3_msg)
                print("%s results has been found!"%count) # 打印匹配结果个数
        else:
            print("您输入的条件不存在，请重新选择")
            continue

        return True

def add():
    '''
    增加用户
    :return:
    '''
    while True:
        # ck_user = auth.check_user()  # 检测用户是否存在，如果存在返回用户已存在和信息
        curr_day = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username = input("用户名>>>:")
        phone = input("手机号>>>:")
        age = input("年龄>>>:")
        vocation = input("职业>>>:")
        company = input("公司名>>>:")

        add_info_dic = {
            'username':username,
            'phone':phone, # 11位
            'age':age,
            'vocation':vocation,
            'company':company,
            'enroll_day':curr_day
        }

        db_file = "%s/%s.json" %(db_path,phone)

        ck_user = auth.check_user(phone) # 检查用户是否存在，手机号唯一

        if ck_user: # 返回非空 手机号唯一判断 存在该手机号
            print("该用户手机号已经存在，请使用其他手机号！")
            continue

        else:
            with open(db_file,'w') as f:
                json.dump(add_info_dic,f)  # 新用户数据写入文件
                print(add_info_dic)  # 打印新增用户信息

                return True


def update():
    '''
    用户信息修改，写回用户db文件，如果修改手机号，在生成新手机号文件之后，删除原手机号的文件
    :return:
    '''
    msg = u'''
    1、用户名
    2、手机号
    3、年龄
    4、职业
    5、公司名称
    '''
    msg_dic = {
    '1':'username',
    '2':'phone', # 11位
    '3':'age',
    '4':'vocation',
    '5':'company',
    '6':'enroll_day'
    }

    #提示输入手机号 (此处需要做位数（11位）限制
    user_phone = input("请输入您要修改的用户手机号>>>:")
    # 判断用户是否存在
    user_info = auth.check_user(user_phone)  # 用户存在则返回用户信息

    #用户数据更改流程
    if user_info: # Not None  返回了用户信息
        print(msg)  # 打印用户操作项
        # 提示用户输入项
        change_item = input("请选择您要修改的项目>>>:") # 3
        change_value = input("请输入您要修改的值>>>:")  # 输入不限制格式

        print("\033[42;1m%s\033[0m" % user_info)  # 打印用户信息

        user_info[msg_dic[change_item]] = change_value  # 给对应的要修改的key 复制 value

        #增加判断，如果修改的是手机号，需要把原手机号文件删除，生成新手机号命名的文件
        if change_item == '2':
            db_file = "%s/%s.json" %(db_path,change_value)
            with open(db_file,'w') as f:
                print(user_info)
                json.dump(user_info,f)

            temp_phone_file = "%s/%s.json" %(db_path,user_phone)
            if os.path.isfile(temp_phone_file):
                os.remove(temp_phone_file)
                print("%s/%s.json 文件已删除"%(db_path,user_phone))

            else:
                return
        # 修改非手机号 选项 正常修改文件
        else:
            db_file = "%s/%s.json" %(db_path,user_phone)
            with open(db_file,'w') as f:
                print(user_info)
                json.dump(user_info,f)
        return True

    else:
        print("\033[42;1m您要修改的用户不存在\033[0m".center(10,'*'))
        return True

def delete():
    '''
    按照输入手机号，删除已存在的手机号文件
    :return:
    '''
    delete_input = input("\033[35;1m请输入您要删除的手机号>>>:\033[0m".strip())
    user_info = auth.check_user(delete_input)

    db_file = "%s/%s.json"%(db_path,delete_input)
    if user_info:
        # if os.path.isfile():
        os.remove(db_file)
        print("用户\033[42;1m [ %s ] \033[0m 已删除 "%(delete_input))
        # return True
    else:
        print("\033[42;1m 您要删除的文件[ %s/%s.json] 不存在"%(db_path,delete_input))
    return True

def log_out():
    '''
    退出函数
    :return:
    '''
    print("\033[31;1mGoodBye!\033[0m".center(50,'-'))
    exit()

