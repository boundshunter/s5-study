__author__ = 'sujunfeng'

shopping_menu=[
    ("Iphone X",8999),
    ("Mac pro",17999),
    ("Bike",999),
    ("Balance car",1999),
    ("Book",59),
    ("IWatch",3999)
]

user_info_dict = {
    'jfsu':{
        'password':'abc123!',
        'salary':30000,
        'buying_list':[]
    },
    'mmm':{
        'password':'123123',
        'salary':50000,
        'buying_list':[]
    }
}

with open('user_info_list.txt','w',encoding="utf-8") as f_init:
    f_init.write(str(user_info_dict))

# new_user_info = {'hanhan':{'password':'abc123','salary':10000000}}

# user_new_dict = dict(user_info_dict,**new_user_info) # 新用户字典和老用户字典合并
# print(user_new_dict)

#new_user_info = {'user_login':{'password''':'new_user_password'','salary':'new_user_salary'}}
import sys
with open("user_info_list.txt",'r') as f:
    info=f.read()
    user_info_dict = eval(info)
#print(user_info_dict)


def shopping_list():  # 打印商品列表
    print('商品列表'.center(50,'-'))
    for menu in shopping_menu:
        #print(menu[1][1])
        print(shopping_menu.index(menu),menu)

user_login = input("请输入您的用户名:")

if user_login in user_info_dict:
    balance = user_info_dict[user_login]['salary']  # 定义用户余额
    print('您的余额为:%s' % balance)  # 显示余额

    shopping_list()  # 打印商品列表
    exit_flag = False
    while not exit_flag:
        choice = int(input("请输入您要购买的商品编号:"))
        if choice < len(shopping_menu) and choice >= 0:
            shopping_item = shopping_menu[choice]
            #print(shopping_item)
            if balance >= shopping_item[1]:  # 金额足够购买商品
                balance = balance - shopping_item[1]
                product_name = shopping_item[0]

                print("您购买的商品是:%s" % product_name)
                print("您的余额为:%s" % balance)
                go_on = input("是否继续购买 y 继续购买，或者按任意键退出:")
                if go_on == 'y':
                    shopping_list()
                    continue
                else:
                    print("您的余额为 %s " % balance)
                    print("您购买的商品为")
                    sys.exit()
            else:
                print("您的余额不足，请充值")
                print("是否充入金额 y 选择充入金额，或者按任意键退出")

else:
    print("您的用户不存在，需要注册!")
    new_user_password = input("请输入您的密码:")  # 输入新用户密码
    exit_flat = False
    while not exit_flat:
        if new_user_password.strip() != "":  # 新密码不为空
            new_user_salary = input("请冲入您的金额:")   # 提示输入金额
            if new_user_salary.isdigit():  # 金额为数字
                new_user_salary=int(new_user_salary)  # 金额变为整形
                new_user_info = {user_login:{'password':new_user_password,'salary':new_user_salary}} # 定义新用户字典信息
                #print(new_user_info)
                user_new_dict = dict(user_info_dict,**new_user_info)    # 合并新用户字典到 所有用户字典

                with open('user_info_list.txt','w',encoding="utf-8") as f_init:
                    user_all_dict = f_init.write(str(user_new_dict))  # 所有用户字典写回用户信息文件

                #print(user_all_dict)
                print('登录成功，欢迎您 %s \n'
                      '您的余额为:%s'% user_login,new_user_salary)
                shopping_list()  # 打印商品列表
                #跳到用户登录，可以继续购买  def user_login()

                break  #退出(暂时，需要添加用户购买流程）
            else:
                print("您的输入不正确，请输入充值金额的数字！")
                break
        else:
            print('您的密码输入不符合要求，请重新输入，或者退出程序，是否退出？')
            logout = input("请输入您的选择Y(退出)/N(继续)")
            if logout != 'y':
                continue
            else:
               exit_flat = True



