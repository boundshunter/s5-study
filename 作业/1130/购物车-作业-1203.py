__author__ = 'sujunfeng'

shopping_menu=[
    ("Iphone X",8999),
    ("Mac pro",17999),
    ("Bike",999),
    ("Balance car",1999),
    ("Book",59),
    ("IWatch",3999)
]

import sys
with open("user_info_list.txt",'r') as f:
    info=f.read()
    user_info_dict = eval(info)

def shopping_list():  # 打印商品列表
    print('\033[31;1m商品列表\033[0m'.center(50,'-'))
    for menu in shopping_menu:
        #print(menu[1][1])
        print(shopping_menu.index(menu),menu)


user_login = input("\033[31;1m请输入您的用户名:\033[0m")  # 输入用户名

if user_login in user_info_dict:
    balance = user_info_dict[user_login]['salary']  # 定义用户余额
    print('\033[42;1m 您的余额为:%s\033[0m' % balance)  # 显示余额

    this_buy = user_info_dict[user_login]['buying_list'] #初始化本次购买记录
    print(this_buy)
    shopping_list()  # 打印商品列表

    exit_flag = False
    while not exit_flag:
        choice = int(input("\033[31;1m请输入您要购买的商品编号:\033[0m"))  # 选择购买商品编号
        if choice < len(shopping_menu) and choice >= 0:   # 判断输入编号是否在购买编号范围内
            shopping_item = shopping_menu[choice]         # 定义购买商品信息
            #print(shopping_item)
            if balance >= shopping_item[1]:  # 判断金额是否足够
                balance = balance - shopping_item[1]    # 金额足够则在原有基础上减去商品金额
                product_name = shopping_item[0]  # 定义购买商品信息

                this_buy.append(product_name)  # 定义本次购买商品信息
                print("\033[42;1m您已购买的商品是:%s\033[0m" % this_buy)
                print("\033[42;1m您的余额为:%s\033[0m" % balance)

                go_on = input("\033[41;1m是否继续购买 按'y'继续购买，或者按任意键退出:\033[0m")
                if go_on == 'y':
                    shopping_list()
                    continue
                else:
                    print("\033[42;1m您的余额为 %s \033[0m" % balance)
                    print("\033[42;1m您购买的商品是:%s \033[0m" % this_buy)

                    #购买状态写入用户文件
                    with open('user_info_list.txt','w') as f:
                        user_info_dict[user_login]['buying_list'] = this_buy  # 用户已购买列表
                        user_info_dict[user_login]['salary'] = balance   # 用户余额
                        #print(str(user_info_dict[user_login]['buying_list']))
                        #print(user_info_dict)
                        f.write(str(user_info_dict))
                    sys.exit()
            else:
                print("\033[41;1m您的余额不足，请充值,您的余额为 %s \033[0m" % balance)
                is_recharge = input("\033[31;1m是否充入金额 y 选择充入金额，或者按任意键退出\033[0m")
                if is_recharge == 'y':
                    user_salary = input("\033[31;1m请充入您的金额:\033[0m")   # 提示输入金额
                    if user_salary.isdigit():  # 金额为数字
                        user_salary=int(user_salary)  # 金额变为整形
                        current_balance = user_salary +  balance # 充值后总金额 =  充值金额 + 余额
                        user_info_dict[user_login]['salary'] = current_balance

                        with open('user_info_list.txt','w',encoding="utf-8") as f_init:
                            f_init.write(str(user_info_dict))  # 所有用户字典写回用户信息文件
                        continue
                    else:
                        print("\033[31;1m您的输入不正确，请输入充值金额的数字！\033[31;1m")
                        break
                else:
                    print("\033[41;1m您的余额为 %s \033[0m" % balance)
                    sys.exit()



else:
    print("\033[31;1m您的用户不存在，需要注册!\033[0m")
    new_user_password = input("\033[31;1m请输入您的密码:\033[0m")  # 输入新用户密码
    exit_flag = False
    while not exit_flag:
        if new_user_password.strip() != "":  # 新密码不为空
            new_user_salary = input("\033[31;1m请充入您的金额:\033[0m")   # 提示输入金额
            if new_user_salary.isdigit():  # 金额为数字
                new_user_salary=int(new_user_salary)  # 金额变为整形
                new_user_info = {user_login:{'password':new_user_password,'salary':new_user_salary}} # 定义新用户字典信息

                user_new_dict = dict(user_info_dict,**new_user_info)    # 合并新用户字典到 所有用户字典

                with open('user_info_list.txt','w',encoding="utf-8") as f_init:
                    user_all_dict = f_init.write(str(user_new_dict))  # 所有用户字典写回用户信息文件

                print('\033[31;1m登录成功，欢迎您 %s 您的余额为:%s\033[0m'% (user_login,new_user_salary))
                shopping_list()  # 打印商品列表
                break  #退出(需要添加跳转到用户购买流程，暂时不会定义函数）
            else:
                print("\033[31;1m您的输入不正确，请输入充值金额的数字！\033[0m")
                exit_flag = False # 跳转到金额输入
        else:
            print('\033[42;1m您的密码输入不符合要求,程序退出\033[0m')
            sys.exit()





