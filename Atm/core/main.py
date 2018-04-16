#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import sys
import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
# from auth import acc_login
import datetime
import time
from core import logger
from core import auth
from core import accounts
from core import transaction
from core import db_handler
from conf import settings

# 定义访问日志
access_logger=logger.logger('access')

# 定义操作日志
transaction_logger = logger.logger('transaction')

# 初始化用户数据
user_data = {
    'account_id':None,
    'is_authorized':False,
    'account_data':None
}

def get_user_data():
    '''
    获取用户数据
    :return: user_data
    '''
    # 获取用户数据，通过用户登录认证，并记录日志
    account_data = auth.acc_login(user_data,access_logger)
    # print("acc_da",account_data)
    #  判断登录状态，返回数据
    if user_data['is_authorized']:
        user_data['account_data'] = account_data
        return user_data
    else:
        return None

def payApi(amount):
    '''
    交易接口，提供给其他消费方式调用
    :param amount:
    :return:
    '''

    amount = int(amount)

    acc_data = get_user_data()
    # print("\033[42;1m payApi \033[0m",acc_data)

    # 根据获取到的用户id 获取用户数据
    account_data = accounts.load_balance(acc_data['account_id'])

    # 判断交易金额 是否大于，交易大于0 则进行交易操作
    if amount > 0:
        new_balance = transaction.make_transaction(transaction_logger,account_data,'pay',amount)
        if new_balance:
            return True
    else:
        print("你的输入 [%s] 有误，请输入数字金额"% amount)
        return None

def withdraw(acc_data):
    '''
    取款，显示余额，判断是否可以取款，记录日志
    :param acc_data:  user_data
    :return:
    '''
    #  根据用户id 打印余额信息
    account_data = accounts.load_balance(acc_data['account_id'])
    balance_info = '''---------余额信息---------\033[33;1m
        Credit:  %s
        Balance: %s
    \033[0m'''% (account_data['credit'],account_data['balance'])
    print(balance_info)

    # RETURN_FLAG = False
    while True:
        print("\033[32;1m --------Tips press [b] to back！--------\033[0m")
        withdraw_amount = input("请输入取款金额>>>:".strip())

        # 根据用户输入，获取为 b 返回上一级
        if withdraw_amount == 'b':
            return True
        # 获取输入金额是否大于0并且为数字，进行取款操作，并记录日志
        elif len(withdraw_amount) > 0 and withdraw_amount.isdigit:
            curr_balance = transaction.make_transaction(transaction_logger,account_data,'withdraw',withdraw_amount)
            time.sleep(1)  # 解决数据返回bug
            # print(curr_balance)
            if curr_balance:
                print("\033[32;1m您当前的余额为:%s\033[0m" % curr_balance['balance'])


        else:
            print("\033[31;1m输入格式错误，只允许输入数字，或 按 [b] 返回！\033[0m")
            continue

def repay(acc_data):
    '''
    还款
    :param acc_data:  user_data
    :return:
    '''
    # 打印余额信息
    account_data = accounts.load_balance(acc_data['account_id'])
    balance_info = '''---------余额信息---------\033[33;1m
        Credit:  %s
        Balance: %s
    \033[0m'''% (account_data['credit'],account_data['balance'])
    print(balance_info)
    while True:
        print("\033[32;1m --------Tips press [b] to back！--------\033[0m")
        repay_amount = input("请输入您的还款金额".strip())

        if repay_amount == 'b':
            return True
        # 判断 还款金额是否为大于0的数字，进行还款交易操作
        elif len(repay_amount) > 0 and repay_amount.isdigit:
            curr_balance = transaction.make_transaction(transaction_logger,account_data,'repay',repay_amount)
            if curr_balance:
                print("\033[32;1m您当前的余额为:%s\033[0m" % curr_balance['balance'])
        else:
            print("\033[31;1m输入格式错误，只允许输入数字，或 按 [b] 返回！\033[0m")
            continue

def transfer(acc_data):
    '''
    用户转账操作
    :param acc_data:
    :return:
    '''
    # 打印余额
    account_data = accounts.load_balance(acc_data['account_id'])
    balance_info = '''---------余额信息---------\033[33;1m
        Credit:  %s
        Balance: %s
    \033[0m'''% (account_data['credit'],account_data['balance'])
    print(balance_info)
    while True:
        # print("\033[32;1m --------Tips press [b] to back！--------\033[0m")
        # 获取 要转入账户ID
        recv_id = input("\033[32;1m请输入要转入的账户ID>>>:\033[0m".strip())

        if auth.check_account(recv_id):  #  True  return  account_data 判断接收账户是否存在和过期
            recv_acc_data = auth.check_account(recv_id)
            # print("recv_acc_data",recv_acc_data)
            if recv_acc_data:  # 被转入账户存在，则获取转入金额
                print("\033[32;1m --------Tips press [b] to back！--------\033[0m")
                trans_amount = input("\033[33;1m请输入转账金额>>>:\033[0m")

                if trans_amount == 'b':
                    return True
                #  判断要转出金额的输入是否为小于 当前余额的数字
                elif float(trans_amount) < account_data['balance'] and trans_amount.isdigit():
                    # 进行转账操作
                    curr_balance = transaction.make_transaction(transaction_logger,account_data,'transfer',trans_amount)
                    # 记录转账日志
                    transaction.make_transaction(transaction_logger,recv_acc_data,'receive',trans_amount)
                    # 转账后显示余额
                    print("您当前的余额为:%s"%curr_balance['balance'])
                    time.sleep(1)
                    return True
                else:
                    print("您输入的金额[%s]过大或者不符合输入要求，请重新输入不超过您余额[%s]的额度"
                          %(trans_amount,account_data['balance']))
                    continue
        else:
            print("\033[31;1m您输入的账户不存在，请重新输入\033[0m")
            continue

def save(acc_data):
    '''
    用户存款操作
    :param acc_data:
    :return:
    '''
    # 获取当前余额信息
    account_data = accounts.load_balance(acc_data['account_id'])
    balance_info = '''---------余额信息---------\033[33;1m
        Credit:  %s
        Balance: %s
    \033[0m'''% (account_data['credit'],account_data['balance'])
    print(balance_info)

    while True:
        print("\033[32;1m --------Tips press [b] to back！--------\033[0m")
        # 获取存入金额
        save_amount = input("请输入存款金额>>>:".strip())

        if save_amount == 'b':
            return True

        # 判断存入金额是否为大于0的数字
        elif len(save_amount) > 0 and save_amount.isdigit:
            # 进行存款操作
            curr_balance = transaction.make_transaction(transaction_logger,account_data,'save',save_amount)
            time.sleep(1)
            # print(curr_balance)
            if curr_balance:
                print("\033[32;1m您当前的余额为:%s\033[0m" % curr_balance['balance'])


        else:
            print("\033[31;1m输入格式错误，只允许输入数字，或 按 [b] 返回！\033[0m")
            continue

def display_bills(acc_data):
    '''
    显示用户账单
    :param acc_data:
    :return:
    '''
    check_date = input("请输入查询日期 \033[31;1meg:[2018-02] \033[0m>>:".strip())  #输入查询日期年月
    log_path = db_handler.db_handler(settings.LOG_DATABASE)   # 日志路径
    bill_file = "%s/%s.bills" % (log_path,acc_data['account_id'])   # 日志文件路径
    print(bill_file)
    # 判断账单文件是否为空
    if os.path.isfile(bill_file):
        print("账户 [\033[32;1m%s\033[0m] 账单:".center(60,'-') % acc_data["account_id"])
        with open(bill_file,'r') as f:
            for bill in f:
                # print("for bills:",bill)
                bill_date = bill.split(' ')[1]  # 取账单月份
                # print(bill_date)

                # 核对查询月份,打印相应账单信息
                if check_date == bill_date:
                    print("\033[33;1m%s\033[0m" % bill.strip())

        log_type = "transaction"
        # 传入account_id 转换成int型，比较大小，获取用户操作日志
        # 根据查询，显示账单
        logger.show_log(int(acc_data['account_id']), log_type, check_date)
        return True

    else:
        print("你的账号[%s]不存在账单" % acc_data['account_id'])
        return True



def log_out(acc_data):
    '''
    普通用户退出
    :param acc_data:
    :return:
    '''
    print("\033[35;1m 亲爱的用户 [%s] ，感谢您使用爱存不存系统，再见！\033[0m".center(50,'-') % acc_data['account_id'])

def interactive(acc_data):
    '''
    用户菜单选项，可查询账户信息，对账户进行存取款转账，查账单等操作
    :param acc_data: 用户数据字典   account_data
    :return:
    '''
    # print("interactive",acc_data)
    # 获取用户状态
    user_state = acc_data['status']
    # 判断用户是否为管理员，管理员id 为8
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

    # 定义 操作类型 字典
    menu_dic = {
        '1':auth.get_user_info,
        '2':withdraw,
        '3':repay,
        '4':transfer,
        '5':save,
        '6':display_bills,
        '7':log_out
    }

    exit_sign = True
    while exit_sign:
        print(menu)
        user_choice = input(">>>:".strip())

        # 根据输入id，执行不同操作类型入口
        if user_choice in menu_dic:
            # print('menu:',user_data)
            exit_sign = menu_dic[user_choice](user_data)  # user_data 传给 acc_data

        else:
            print("\033[31;1m您输入的选项有误，请重新输入\033[0m")
            continue

def check_admin(func):
    """
    检查是否管理员
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        if user_data['account_data'].get('status', None) == 8:
            ret = func(*args, **kwargs)
            return ret
        else:
            access_logger.error("Your account [%s] is not a admin,please use a admin account to login system"
                                % user_data['account_id'])
    return inner

@check_admin
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
        print("\033[33;1m%s\033[0m" % menu)
        user_choice = input(">>>>:")

        # 根据输入选项，执行管理员操作入口
        if user_choice in menu_dict:
            # print(menu_dict[user_choice])
            go_flag = eval(menu_dict[user_choice])

        else:
            print("\033[31;1m您输入的选项有误，请重新输入\033[0m")
            continue


def exit_flag():
    '''
    退出
    :return:
    '''
    print("----退出当前管理员[%s]----"%user_data['account_id'])
    exit()

def get_user_bill(account_id):
    '''
    获取用户账单
    :param account_id:
    :return:
    '''
    i = datetime.datetime.now()  # 当前时间
    year_month = "%s" % (datetime.datetime.strftime(i,"%Y-%m"))  # 帐单年月
    account_data = accounts.load_balance(account_id)  # 获取帐户信息
    balance = account_data["balance"]  # 可用额度
    credit = account_data["credit"]  # 信用额度
    if i.day != settings.BILL_DAY:
        print("\033[31;1mToday is not the bill generation day!\033[0m")
        # return    # 此处为了演示，先注释

    # 判断额度，判定是否提示还款
    if balance >= credit:
        repay_amount = 0
        bill_info = "Account [\033[32;1m%s\033[0m] needn't to repay." % account_id
    else:
        repay_amount = credit - balance
        bill_info = "Account [\033[32;1m%s\033[0m] need to repay [\033[33;1m%s\033[0m]" \
                    % (account_id, repay_amount)

    print(bill_info)
    log_path = db_handler.db_handler(settings.LOG_DATABASE)
    bill_log = "%s/%s.bills" % (log_path, account_id)
    # 记录账单信息
    with open(bill_log, "a+") as f:
        f.write("bill_date: %s account_id: %s need_repay: %d\n" % (year_month, account_id, repay_amount))

def get_all_bills():
    '''
    获取所有用户账单信息
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    # 获取路径，目录，文件名称
    for root, dirs, files in os.walk(db_path):
        print("root:%s, dirs:%s files:%s" % (root,dirs,files))
        for f in files:
            # 判断是否存在.json结尾的文件
            if os.path.splitext(f)[1] == ".json":
                # 获取账户ID
                account_id = os.path.splitext(f)[0]  # 帐户id
                # account_file = "%s/%s.json" % (db_path, account_id)
                # account_data = auth.check_account(account_id)  # 获取用户信息
                account_data = auth.ck_acc_data(account_id)
                # 判断用户权限是否为管理员
                if account_data:
                    status = account_data['status']
                    # print(status)
                    print("Account bill:".center(50, "-"))

                    # 除了管理员，普通帐户都应该出帐单，即使帐户禁用
                    if status != 8:
                        # print("status != 8 ",account_id)
                        auth.display_account_info(account_data)
                        get_user_bill(account_id)  # 获取帐单
                        print("End".center(50, "-"))
    return True

# def login():
#     print("Welcome to my homepage.")

def manager_run():
    '''
    管理员入口判断
    :return:
    '''
    print("\033[31;1m ATM管理员菜单 \033[0m".center(50,'#'))
    user_data = get_user_data()
    status = user_data['account_data']['status']
    # if status == 8: # 判断管理员权限
    #     manager_controll(user_data)
    # else:
    #     access_logger.error("Your account [%s] is not a admin,please use a admin account to login system"
    #                         % user_data['account_id'])
    #     exit()
    manager_controll(user_data)

def run():
    '''
    普通用户入口判断
    :return:
    '''
    print("\033[31;1m ATM用户菜单 \033[0m".center(50,'#'))
    user_data = get_user_data()

    if user_data:  # 判断用户数据返回非空
        acc_data = user_data['account_data']
        # 执行用户交互
        interactive(acc_data)  # account_data
    else:
        exit()
