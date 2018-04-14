#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# import os
import sys
import datetime
import re
# BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

from core import auth
from core import accounts
from conf import goods

# 初始化购物车
shopCar = {}

#初始化用户数据
user_data = {
    'is_authorized':None,
    'account_data':None
}

def userLogin():
    '''
    用户登录入口，登录会判断用户是否存在，登录密码是否正确，用户判断是根据用户注册成功后每个用户生成的以用户名命名的
    数据文件内容做校验。
    :return:
    '''
    account = input("请输入用户名: ".strip())
    password = input("请输入密码: ".strip())

    # 检测用户是否存在 返回用户数据，不存在 返回 None
    acc_data = auth.check_account(account,password)

    # 判断用户数据是否为空 非空 则 返回用户数据
    if acc_data is not None:
        user_data['account_data'] = acc_data
        # user_data['is_authorized'] = yes
        return user_data
    else:
        exit()

def userRegist():
    '''
    用户注册入口，用户注册时判断用户是否存在，用户不存在则注册，写入注册用户数据文件，数据文件以用户名命名
    :return:
    '''
    # 定义当前时间
    curr_day = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 注册循环流程
    while True:
        account = input("请输入用户名：".strip())
        password = input("请输入密码：".strip())

        #  注册前判断用户是否存在
        acc_data = auth.check_account(account,password)

        #  用户数据非空，则用户存在
        if acc_data is not None:
            print("\033[42;1m 用户[%s]已存在，请使用其他用户重新注册\033[0m".center(20,'*') % account)

        else:
            # 用户模板文件
            acc_template = {
                'enroll_date': curr_day,
                'user': account,
                'password': password,
                'status': 0,
                'balance': 50000.0,
             }

            # 用户数据序列化到文件
            accounts.dumpAccount(acc_template)

            # 打印用户注册信息
            registInfo = '''
            注册日期：%s
            用户名：%s
            密码：%s
            余额：%s
            '''%(curr_day,acc_template['user'],acc_template['password'],acc_template['balance'])
            print(registInfo)
        return True

def userLogout():
    '''
    退出选项
    :return:
    '''
    sys.exit("Thanks for shopping，Byebye.")

def interactive():
    '''
    用户交互入口
    :return:
    '''
    info = '''
    ---------用户选项----------
    1、登录
    2、注册
    3、退出
    '''
    menu_dic = {
        '1':'userLogin()',
        '2':'userRegist()',
        '3':'userLogout()'
    }

    flag = True
    while flag:
        print("\033[35;1m %s \033[0m" % info)
        choice = input("输入您的选项：".strip())

        #  根据用户输入选项 进入 登录，注册，退出 流程
        if choice in menu_dic:
            flag = eval(menu_dic[choice])
            # print('flag---------------',flag)
            return True
        else:
            print("\033[35;1m输入选项有误，请重新运行程序\033[0m")
            exit()

def go_shopping():
    '''
    购物流程:1、根据用户输入，返回物品列表，2、加入购物车之前判断用户余额，余额充足直接扣款，扣款后提示剩余余额
    3、余额不足则提示充值，充值调用ATM接口（调用接口为本次实现关键）
    :return:
    '''
    # 购物开始
    shopList1 = '''
    --------------物品分类----------------
    1、electronic product（电子产品）
    2、drink (饮品）
    3、household appliances（家用电器）
    '''
    shopListMenu1 = {
        '1':'listL1()',
        '2':'listL2()',
        '3':'listL3()'
    }
    go_flag = True
    while  go_flag:
        print("\033[35;1m%s\033[0m" % shopList1)
        print("\033[33;1m按[q]退出程序，按[b]返回上一级！\033[0m")
        Choice = input('L1请输入您的选择(编号):'.strip())
        if Choice in shopListMenu1:
            go_flag = eval(shopListMenu1[Choice])
        elif Choice == 'q':
            sys.exit("感谢您的购物，再见！")
        elif Choice == 'b':
            interactive()
        else:
            print("您的选项有误，请重新选择！")
            continue

def listShopcar():
    '''
    显示购物车商品和价格,判断是否购物，购物车位空，则不显示购物列表
    :return:
    '''
    #  判断购物车是否为空
    if shopCar:  # Not None
        print(" 本次购买商品列表 ".center(40,'-'))
        for k,v in shopCar.items():
            print("    "+"商品名称："+k+" ---- "+"价格："+v)
    else:
        return None


def listL1():
    '''
    购物流程，显示购物车
    :return:
    '''
    L1_Info = goods.L1_Info
    L1_Info_Dic = goods.L1_Info_Dic

    L1_flag = True
    while L1_flag:

        acc_data = user_data['account_data']
        print("\033[31;1m%s\033[0m" % L1_Info)
        print("\033[33;1m输入[b] 返回上一级，输入[q] 退出程序 \033[0m")

        choice = input("L2请输入您要购买的产品编号：")
        if choice in L1_Info_Dic:

            if float(L1_Info_Dic[choice][1]) > acc_data['balance']:
                charge_YN = input("您的余额不足，是否充值,按'y'进行充值，其他任意键继续购物!".strip())

                if charge_YN == 'y':
                    charge = input("请输入您要充值的金额:".strip())
                    acc_data['balance'] = acc_data['balance'] + float(charge)
                    accounts.dumpAccount(acc_data)
                    shopCar[L1_Info_Dic[choice][0]] = L1_Info_Dic[choice][1]
                    print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])
                    #增加 记录充值 操作日志的记录, settings 行为字典，充值，花费 金额 等等
                    # print("shopCar")
                else:
                    continue

            else:
                #余额足够，购买对应编号商品，余额-商品金额，将购买后余额写入用户数据文件
                acc_data['balance'] = acc_data['balance'] - float(L1_Info_Dic[choice][1])
                accounts.dumpAccount(acc_data)
                shopCar[L1_Info_Dic[choice][0]] = L1_Info_Dic[choice][1]
                print("\n")
                listShopcar()
                print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])
        elif choice == 'q':
            listShopcar()
            sys.exit("感谢您的购物，再见！")
        elif choice == 'b':
            # 返回上一层
            return True

        else:
            print("L2您输入的产品编号有误，请重新输入")
            continue

def listL2():
    '''
    购物流程，显示购物车
    :return:
    '''
    L2_Info = goods.L2_Info
    L2_Info_Dic = goods.L2_Info_Dic

    L2_flag = True
    while L2_flag:

        acc_data = user_data['account_data']
        print("\033[31;1m%s\033[0m" % L2_Info)
        print("\033[33;1m输入[b] 返回上一级，输入[q] 退出程序 \033[0m")

        choice = input("L2请输入您要购买的产品编号：")
        if choice in L2_Info_Dic:

            if float(L2_Info_Dic[choice][1]) > acc_data['balance']:
                charge_YN = input("您的余额不足，是否充值,按'y'进行充值，其他任意键继续购物!".strip())

                if charge_YN == 'y':
                    charge = input("请输入您要充值的金额:".strip())
                    acc_data['balance'] = acc_data['balance'] + float(charge)
                    accounts.dumpAccount(acc_data)
                    shopCar[L2_Info_Dic[choice][0]] = L2_Info_Dic[choice][1]
                    print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])
                    #增加 记录充值 操作日志的记录, settings 行为字典，充值，花费 金额 等等
                    # print("shopCar")
                else:
                    continue

            else:
                #余额足够，购买对应编号商品，余额-商品金额，将购买后余额写入用户数据文件
                acc_data['balance'] = acc_data['balance'] - float(L2_Info_Dic[choice][1])
                accounts.dumpAccount(acc_data)
                shopCar[L2_Info_Dic[choice][0]] = L2_Info_Dic[choice][1]
                print("\n")
                listShopcar()
                print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])

        elif choice == 'q':
            listShopcar()
            sys.exit("感谢您的购物，再见！")
        elif choice == 'b':
            # 返回上一层
            return True

        else:
            print("L2您输入的产品编号有误，请重新输入")
            continue

def listL3():
    '''
    购物流程，显示购物车
    :return:
    '''
    L3_Info = goods.L3_Info
    L3_Info_Dic = goods.L3_Info_Dic

    L3_flag = True
    while L3_flag:

        acc_data = user_data['account_data']
        print("\033[31;1m%s\033[0m" % L3_Info)
        print("\033[33;1m输入[b] 返回上一级，输入[q] 退出程序 \033[0m")

        choice = input("L2请输入您要购买的产品编号：")
        if choice in L3_Info_Dic:

            if float(L3_Info_Dic[choice][1]) > acc_data['balance']:
                charge_YN = input("您的余额不足，是否充值,按'y'进行充值，其他任意键继续购物!".strip())

                if charge_YN == 'y':
                    charge = input("请输入您要充值的金额:".strip())
                    acc_data['balance'] = acc_data['balance'] + float(charge)
                    accounts.dumpAccount(acc_data)
                    shopCar[L3_Info_Dic[choice][0]] = L3_Info_Dic[choice][1]
                    print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])

                else:
                    continue

            else:
                #余额足够，购买对应编号商品，余额-商品金额，将购买后余额写入用户数据文件
                acc_data['balance'] = acc_data['balance'] - float(L3_Info_Dic[choice][1])
                accounts.dumpAccount(acc_data)
                shopCar[L3_Info_Dic[choice][0]] = L3_Info_Dic[choice][1]
                print("\n")
                listShopcar()
                # 增加 记录 购物历史 的 操作日志,显示购物车
                print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])
        elif choice == 'q':
            listShopcar()
            sys.exit("感谢您的购物，再见！")
        elif choice == 'b':
            # 返回上一层
            return True

        else:
            print("L2您输入的产品编号有误，请重新输入")
            continue

def run():
    '''
    主程序运行入口
    :return:
    '''
    interactive()
    # 登录成功后，拿到用户信息，登录失败后，用户信息为None
    print("交互",user_data)
    go_shopping()
