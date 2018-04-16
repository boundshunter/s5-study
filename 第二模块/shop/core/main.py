#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import sys
import datetime
import subprocess

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

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

# 支付接口调用 方式
atm_api = os.path.dirname(BASE_DIR) + "/Atm/api/pay_api.py"


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
            return True
        else:
            print("\033[35;1m输入选项有误，请重新运行程序\033[0m")
            exit()

def go_shopping():
    '''
    购物流程，选择品类之后进入二级详细商品列表进行购物
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
        # 显示商品类别
        print("\033[35;1m%s\033[0m" % shopList1)
        print("\033[33;1m按[q]退出程序，按[b]返回上一级！\033[0m")
        Choice = input('L1请输入您的选择(编号):'.strip())

        #  判断选项是否在商品类别中，存在则就行执行 下一级商品菜单展示，否则退出程序
        if Choice in shopListMenu1:
            go_flag = eval(shopListMenu1[Choice])
        elif Choice == 'q':
            sys.exit("感谢您的购物，再见！")

        #  根据用户程序判断 b 返回上一级
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

        #  购物车非空 显示购买商品名称和价格
        for k,v in shopCar.items():
            print("    "+"商品名称："+k+" ---- "+"价格："+v)
    else:
        return None

def listL1():
    '''
    购物流程，显示购物车内容，购物前判断余额是否充足，不足则提示充值，充值调用ATM接口
    :return:
    '''
    # 获取商品列表 和 价格
    L1_Info = goods.L1_Info
    L1_Info_Dic = goods.L1_Info_Dic

    L1_flag = True
    while L1_flag:

        # 初始化用户数据
        acc_data = user_data['account_data']

        # 打印 商品列表 ，提示用户信息
        print("\033[31;1m%s\033[0m" % L1_Info)
        print("\033[33;1m输入[b] 返回上一级，输入[q] 退出程序 \033[0m")

        #  进入商品购买流程
        choice = input("L2请输入您要购买的产品编号：")

        # 判断选择是否在列表中
        if choice in L1_Info_Dic:
            # 判断金额是否足以购买商品
            if float(L1_Info_Dic[choice][1]) > acc_data['balance']:
                charge_YN = input("您的余额不足，是否充值,按'y'进行充值，其他任意键继续购物!".strip())
                print("\033[41;1m请使用您的银行账号进行充值！\033[0m")

                # 判断 是否 充值 'y' 为进行充值操作
                if charge_YN == 'y':
                    #  调用 支付 接口 充值
                    charge = input("请输入您要充值的金额:".strip())
                    #  判断输入金额是否为数字
                    if charge.isdigit():

                        #  定义  接口文件和金额
                        comm = "python " + atm_api + " " + charge
                        # 创建 调用进程，执行指定的comm
                        pgm = subprocess.Popen(comm,shell=True)
                        # 接口文件交互
                        pgm.communicate()
                        if pgm.returncode == 0:
                            print("\033[31;1m付款成功\033[0m")
                            # 充值成功后，更新用户余额
                            acc_data['balance'] += float(charge)
                            # 将用户余额存入账户
                            accounts.dumpAccount(acc_data)
                            print("您的余额为:%s"%acc_data['balance'])

                        else:
                            print("充值失败！")

                    else:
                        print("你的输入[%s]有误，请输入数字！" % charge)

                else:
                    continue

            else:
                # 余额足够，购买对应编号商品，余额-商品金额，将购买后余额写入用户数据文件
                acc_data['balance'] -= float(L1_Info_Dic[choice][1])
                # 更新后余额存入账户
                accounts.dumpAccount(acc_data)
                #  将购买商品加入购物列表
                shopCar[L1_Info_Dic[choice][0]] = L1_Info_Dic[choice][1]
                print("\n")
                #  打印购物车
                listShopcar()
                print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])
        elif choice == 'q':
            # 打印购物车
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
    购物流程，显示购物车内容，购物前判断余额是否充足，不足则提示充值，充值调用ATM接口
    :return:
    '''
    # 获取商品列表 和 价格
    L2_Info = goods.L2_Info
    L2_Info_Dic = goods.L2_Info_Dic

    L2_flag = True
    while L2_flag:

        # 初始化用户数据
        acc_data = user_data['account_data']

        # 打印 商品列表 ，提示用户信息
        print("\033[31;1m%s\033[0m" % L2_Info)
        print("\033[33;1m输入[b] 返回上一级，输入[q] 退出程序 \033[0m")

        #  进入商品购买流程
        choice = input("L2请输入您要购买的产品编号：")

        # 判断选择是否在列表中
        if choice in L2_Info_Dic:
            # 判断金额是否足以购买商品
            if float(L2_Info_Dic[choice][1]) > acc_data['balance']:
                charge_YN = input("您的余额不足，是否充值,按'y'进行充值，其他任意键继续购物!".strip())
                print("\033[41;1m请使用您的银行账号进行充值！\033[0m")

                # 判断 是否 充值 'y' 为进行充值操作
                if charge_YN == 'y':
                    #  调用 支付 接口 充值
                    charge = input("请输入您要充值的金额:".strip())
                    #  判断输入金额是否为数字
                    if charge.isdigit():

                        #  定义  接口文件和金额
                        comm = "python " + atm_api + " " + charge
                        # 创建 调用进程，执行指定的comm
                        pgm = subprocess.Popen(comm,shell=True)
                        # 接口文件交互
                        pgm.communicate()
                        if pgm.returncode == 0:
                            print("\033[31;1m付款成功\033[0m")
                            # 充值成功后，更新用户余额
                            acc_data['balance'] += float(charge)
                            # 将用户余额存入账户
                            accounts.dumpAccount(acc_data)
                            print("您的余额为:%s"%acc_data['balance'])

                        else:
                            print("充值失败！")

                    else:
                        print("你的输入[%s]有误，请输入数字！" % charge)

                else:
                    continue

            else:
                # 余额足够，购买对应编号商品，余额-商品金额，将购买后余额写入用户数据文件
                acc_data['balance'] -= float(L2_Info_Dic[choice][1])
                # 更新后余额存入账户
                accounts.dumpAccount(acc_data)
                #  将购买商品加入购物列表
                shopCar[L2_Info_Dic[choice][0]] = L2_Info_Dic[choice][1]
                print("\n")
                #  打印购物车
                listShopcar()
                print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])
        elif choice == 'q':
            # 打印购物车
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
    购物流程，显示购物车内容，购物前判断余额是否充足，不足则提示充值，充值调用ATM接口
    :return:
    '''
    # 获取商品列表 和 价格
    L3_Info = goods.L3_Info
    L3_Info_Dic = goods.L3_Info_Dic

    L3_flag = True
    while L3_flag:

        # 初始化用户数据
        acc_data = user_data['account_data']

        # 打印 商品列表 ，提示用户信息
        print("\033[31;1m%s\033[0m" % L3_Info)
        print("\033[33;1m输入[b] 返回上一级，输入[q] 退出程序 \033[0m")

        #  进入商品购买流程
        choice = input("L2请输入您要购买的产品编号：")

        # 判断选择是否在列表中
        if choice in L3_Info_Dic:
            # 判断金额是否足以购买商品
            if float(L3_Info_Dic[choice][1]) > acc_data['balance']:
                charge_YN = input("您的余额不足，是否充值,按'y'进行充值，其他任意键继续购物!".strip())
                print("\033[41;1m请使用您的银行账号进行充值！\033[0m")

                # 判断 是否 充值 'y' 为进行充值操作
                if charge_YN == 'y':
                    #  调用 支付 接口 充值
                    charge = input("请输入您要充值的金额:".strip())
                    #  判断输入金额是否为数字
                    if charge.isdigit():

                        #  定义  接口文件和金额
                        comm = "python " + atm_api + " " + charge
                        # 创建 调用进程，执行指定的comm
                        pgm = subprocess.Popen(comm,shell=True)
                        # 接口文件交互
                        pgm.communicate()
                        if pgm.returncode == 0:
                            print("\033[31;1m付款成功\033[0m")
                            # 充值成功后，更新用户余额
                            acc_data['balance'] += float(charge)
                            # 将用户余额存入账户
                            accounts.dumpAccount(acc_data)
                            print("您的余额为:%s"%acc_data['balance'])

                        else:
                            print("充值失败！")

                    else:
                        print("你的输入[%s]有误，请输入数字！" % charge)

                else:
                    continue

            else:
                # 余额足够，购买对应编号商品，余额-商品金额，将购买后余额写入用户数据文件
                acc_data['balance'] -= float(L3_Info_Dic[choice][1])
                # 更新后余额存入账户
                accounts.dumpAccount(acc_data)
                #  将购买商品加入购物列表
                shopCar[L3_Info_Dic[choice][0]] = L3_Info_Dic[choice][1]
                print("\n")
                #  打印购物车
                listShopcar()
                print("您当前余额 >>>: [ \033[42;1m%s\033[0m ] "%acc_data['balance'])
        elif choice == 'q':
            # 打印购物车
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
    # 用户交互 入口
    interactive()
    #  登录成功后，拿到用户信息，登录失败后，用户信息为None，成功进入购物流程
    go_shopping()
