#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# import sys
# import os
# BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
# sys.path.append(BASE_DIR)
# from auth import acc_login
import datetime
from core import logger
from core import auth
from core import accounts
from core import transaction


access_logger=logger.logger('access')
transaction_logger = logger.logger('transaction')
user_data = {
    'account_id':None,
    'is_authorized':False,
    'account_data':None
}

def get_user_data():
    account_data = auth.acc_login(user_data,access_logger)
    print("acc_da",account_data)
    if user_data['is_authorized']:
        user_data['account_data'] = account_data
        return user_data
    else:
        return None

def withdraw(acc_data):
    '''
    显示余额，判断是否可以取款，记录日志
    :param acc_data:  user_data
    :return:
    '''
    account_data = accounts.load_balance(acc_data['account_id'])
    balance_info = '''---------余额信息---------
            Credit:  %s
            Balance: %s
    '''% (account_data['credit'],account_data['balance'])
    print(balance_info)

    RETURN_FLAG = False
    while not RETURN_FLAG:
        print("\033[32;1m --------Tips press [b] to back！--------\033[0m")
        withdraw_amount = input("请输入取款金额>>>:".strip())
        if  len(withdraw_amount) > 0 and withdraw_amount.isdigit:
            curr_balance = transaction.make_transaction(transaction_logger,account_data,'withdraw',withdraw_amount)
            if curr_balance:
                # print("当前余额信息:%s"
                #       %(balance_info))
                print("curr_balance:",curr_balance)
        elif withdraw_amount == 'b':
            RETURN_FLAG = True

        else:
            print("输入格式错误，只允许输入数字！")

def repay(acc_data):
    '''
    还款
    :param acc_data:  user_data
    :return:
    '''



def transfer(acc_data):
    pass

def save(acc_data):
    pass

def pay_bills(acc_data):
    pass

def interactive(acc_data):
    '''
    用户数据交互
    :param acc_data: 用户数据字典   account_data
    :return:
    '''
    # print("interactive",acc_data)
    user_state = acc_data['status']
    if user_state == 8:
        exit("\033[31;1m 账户 [%s] 为管理员,请使用管理员登录入口! \033[0m"
             % (acc_data['id']) )
    menu = u'''
    ------爱存不存 BANK-------\033[32;1m
    1、账户信息
    2、取款
    3、还款
    4、转账
    5、存款
    6、账单
    7、退出
    \033[0m'''

    menu_dic = {
        '1':auth.get_user_info,
        '2':withdraw,
        '3':repay,
        '4':transfer,
        '5':save,
        '6':pay_bills,
        '7':exit
    }

    exit_sign = True
    while exit_sign:
        print(menu)
        user_choice = input(">>>:".strip())
        if user_choice in menu_dic:
            # print(menu_dict[user_choice])
            print('menu:',user_data)
            exit_sign = menu_dic[user_choice](user_data)  # user_data 传给 acc_data

        else:
            print("\033[31;1m您输入的选项有误，请重新输入\033[0m")
            continue




def manager_controll(user_data):
    '''
    管理员菜单选项
    :param user_data: 用户数据字典
    :return:
    '''
    menu = u'''
    -----------管理员 选项------------
    1、添加用户
    2、查询用户信息
    3、修改用户信息（冻结账户，信用额度等）
    4、生成全部账单
    5、退出
    '''
    menu_dict = {
        '1':"auth.sign_up()",
        '2':"auth.account_info()",
        '3':"auth.account_modify()",
        '4':"get_all_bills()",
        '5':"exit_flag()"
    }
    go_flag = True
    while go_flag:
        print("\033[33;1m%s\033[0m]" % menu )
        user_choice = input(">>>>:")

        if user_choice in menu_dict:
            # print(menu_dict[user_choice])
            go_flag = eval(menu_dict[user_choice])

        else:
            print("\033[31;1m您输入的选项有误，请重新输入\033[0m")
            continue


def exit_flag():
    print("----退出当前管理员[%s]----"%user_data['account_id'])
    exit()

def get_user_bill(account_id):
    curr_day = datetime.datetime.now()


def get_all_bills():
    pass

def login():
    print("Welcome to my homepage.")

# def run():
#     '''
#     程序开始会调用此方法用于和用户数据交互
#     :return:
#     '''
#     acc_data = auth.acc_login(user_data,access_logger)

def manager_run():
    print("\033[31;1m ATM管理员菜单 \033[0m".center(50,'#'))
    user_data = get_user_data()
    # print(user_data)
    manager_controll(user_data)


def run():
    print("\033[31;1m ATM用户菜单 \033[0m".center(50,'#'))
    user_data = get_user_data()
    print("run",user_data)
    acc_data = user_data['account_data']
    interactive(acc_data)  # account_data

