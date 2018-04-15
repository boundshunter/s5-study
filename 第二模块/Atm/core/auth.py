#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
# import sys
# BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
# sys.path.append(BASE_DIR)
import json
import datetime
import hashlib
from core import db_handler
from conf import settings
from core import accounts

def acc_auth(account,password):
    '''
    用户认证（根据用户输入账户，密码）
    :param account:
    :param password:
    :return: account_data
    '''
    #  获取用户数据文件位置
    db_path = db_handler.db_handler(settings.DATABASE)  # settings.DATABASE = conn_parms
    account_file = "%s/%s.json" % (db_path, account)
    # print(db_path)
    # print(account_file)
    # 判断用户文件是否存在，存在则加载用户数据
    if os.path.isfile(account_file): #
        with open(account_file,'r') as f:
            account_data = json.load(f)
            # print(account_data)

        #  判断用户数据文件中密码是否正确
        if account_data['password'] == password:

            exp_time_stamp = datetime.datetime.strptime(account_data['expire_date'],'%Y-%m-%d')

            '''

           '''
            #  获取用户状态
            status = account_data['status']

            #  判断用户是否过期
            if datetime.datetime.now() > exp_time_stamp:
                # print(datetime.datetime.now(),exp_time_stamp)
                print("\033[32;1m您的账户 [%s] 已于 [%s] 过期，请联系管理员申请新卡！\033[0m" % (account,account_data['expire_date']) )

            #  判断是否为管理员账户
            elif status == 0  or status == 8:
                # print(account_data)
                return account_data
            else:  # status 状态不正常
                print("\033[31;1m您的账户状态[%s]有误，请联系管理员,系统退出！\033[0m" % status )
                exit()
        else:
            print("\033[32;1m您的密码有误,请重新输入\033[0m")
    else:
        print(" 您的账户\033[33;1m [%s] \033[0m不存在" % account )


def acc_login(user_data,log_obj):
    '''
    判断用户登录错误次数，超过3次记录日志和打印屏幕输出，使用字典方式支持多用户互相切换错误记录
    :param user_data:
    :param log_obj: access_logger
    :return: auth  =  account_data
    '''
    account_login_dic = {}
    retry_count = 0
    exit_count = 4


    while user_data['is_authorized'] is False and retry_count < exit_count:
        account = input('\033[32;1m请输入账户ID:\033[0m'.strip())
        password = input('\033[32;1m请输入密码:\033[0m'.strip())

        #  判断用户正确性，用户正确则初始化用户数据状态
        auth = acc_auth(account,password)
        if auth:
            user_data['is_authorized'] = True
            user_data['account_id'] = account
            return auth
        else:
            #先检测 dic 里面是否有相同名称 的key，没有就增加，有就取value
            if account not in account_login_dic:  # 如果账户不存在于字典
                count = 0
                count += 1
                account_login_dic.update({account:count}) # 初始化新用户到字典
            else:
                count = account_login_dic[account]  # 初始化 计数
                count += 1                          # 到此处错误已经产生，错误次数+1
                account_login_dic.update({account:count})  # 将用户对应错误次数更新到字典
                # print("old",account_login_dic)
                for i in account_login_dic.values():  # 判断字典中用户名对应的 错误次数
                    retry_count = i
                    # print(retry_count)
                    if retry_count == 3:  # 判断用户是否产生3次错误，3次错误 记录日志 并且 退出当前程序
                        curr_account = list(account_login_dic.keys())[list(account_login_dic.values()).index(retry_count)]
                        # print(curr_account)
                        #  记录用户错误行为日志
                        log_obj.error(" [%s] have try too many attempts,System exit!" % (curr_account))
                        exit()

def sign_up():
    '''
    新用户注册
    :return:
    '''
    exist_flag = True
    while exist_flag is True:
        account = input("请输入用户ID:".strip())
        password =input("请输入密码:".strip())
        user_exist = check_account(account)

        #  用户存在
        if user_exist:  # not None
            print("用户[%s]已存在，请输入其他用户ID" % account)
            exit_flag = True
            # continue

        #  用户不存在
        else:
            curr_day = datetime.datetime.now().strftime("%Y-%m-%d")  #  当前日期
            yesterday = datetime.datetime.now() + datetime.timedelta(days=-1)  #  昨天日期
            after_3_years_day = yesterday.replace(year=(int(yesterday.strftime("%Y")) + 3))  # 三年后的昨天（过期时间）
            expire_day = after_3_years_day.strftime('%Y-%m-%d')   # 过期日期
            pay_day = 22  # 还款日

            account_data = {
                        'enroll_date': curr_day,
                        'password': password,
                        'id': account,
                        'credit': 15000,
                        'status': 0,
                        'balance': 0.0,
                        'expire_date': expire_day,
                        'pay_day': pay_day
             }
            #  存储新用户数据
            accounts.dump_account(account_data)
            print("\033[32;1m账户 [%s] 创建成功，\033[0m" % account)
            print("账户信息:", account_data)
            return True  # 跳出当前循环

def account_info():
    '''
    用户信息查询
    :return:
    '''
    while True:
        account = input("账户ID>>>:".strip())
        account_data = check_account(account)  # True  return account_data
        #  检测用户，判断是否存在
        if account_data:  # not None    is  account_data
            # print(account_data)
            # 用户存在，调用显示用户数据方法
            display_account_info(account_data)
            return True
        else:  # 用户不存在，提示信息
            print("您查询的账户[%s] 不存在" % account)
            return True


def get_user_info(acc_data):
    '''
    获取用户信息，根据传入用户数据
    :param acc_data:  acc_data == user_data
    :return:
    '''

    while True:
        # account = input("账户ID>>>:".strip())
        account = acc_data['account_data']['id']
        account_data = check_account(account)  # True  return account_data
        # print("get_user_info",account_data)

        #  判断用户是否存在，用户存在，调用显示用户数据方法，不存在提示信息
        if account_data:  # not None    is  account_data
            # print(account_data)
            display_account_info(account_data)
            return True
        else:
            print("您查询的账户[%s] 不存在" % account)
            return True

def display_account_info(account_data):
    '''
    显示用户信息
    :param account_data:
    :return True:
    '''
    account_data['password']=get_md5(account_data['password'].encode("utf-8")) # 用户密码加密
    for k in account_data:
        print("{:<20}:\033[32;1m{:<20}\033[0m".format(k,account_data[k]))
    return True

def get_md5(password):
    '''
    用户密码加密
    :param password:
    :return:
    '''
    # 获取 md5
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()


def account_modify():
    '''
    修改账户信息
    :return:
    '''
    retry_count = 0
    items = ['enroll_date','password','id','credit','status','balance','expire_date','pay_day']
    while True:
        account = input("输入要修改的账户ID>>>:")
        acc_data = check_account(account)   # 判断用户可用性
        db_path = db_handler.db_handler(settings.DATABASE)  # settings.DATABASE = conn_parms
        account_file = "%s/%s.json" % (db_path, account)
        if acc_data:  # Not None
            #  用户存在显示用户信息
            display_account_info(acc_data)
            # print(type(acc_data))

            while True:
                input_item = input("请选择您要修改的项目>>>:")
                input_value = input("请输入您要修改的值>>>:")
                # 修改账户信息
                acc_data[input_item] = input_value
                account_data = acc_data
                print("\033[31;1m您已将账户ID为[%s] 中项目 [%s] 值修改为 [%s] !\033[0m" % (account,input_item,input_value))
                # 修改数据写回用户ID数据文件
                accounts.dump_account(account_data)
                return True
        else:
            print("您要修改的用户 [%s] 不存在！" % account)
            return True


def check_account(account):
    '''
    检查用户是否存在，做用户权限是否为管理员判断
    :param account:用户ID
    :return: account_data
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account)

    #  根据用户数据文件，判断用户是否存在
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            status = account_data['status']
            # 判断用户权限
            if status == 8:
                print("权限不足，账户[%s]为管理员,无法查看." % account_data['id'])
                return False

            exp_time_stamp = datetime.datetime.strptime(account_data['expire_date'],"%Y-%m-%d")
            curr_time = datetime.datetime.now()
            #  判断账户是否过期
            if  curr_time > exp_time_stamp:
                print("账户 [%s] 已过期!" % account)
                return False
            #  未过期返回用户数据
            else:
                return account_data
    else:
        return False

def ck_acc_data(account):
    '''
    检查用户是否存在,不做用户权限判断
    :param account:用户ID
    :return: account_data
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account)

    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            status = account_data['status']
            # if status == 8:
            #     print("权限不足，账户[%s]为管理员,无法查看." % account_data['id'])
            #     return False

            exp_time_stamp = datetime.datetime.strptime(account_data['expire_date'],"%Y-%m-%d")
            curr_time = datetime.datetime.now()
            if  curr_time > exp_time_stamp:
                print("账户 [%s] 已过期!" % account)
                return False
            else:
                return account_data
    else:
        return False
