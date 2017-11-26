# def init():
#     # 系统初始化,读所有商品信息,保存到一个全局变量中

import os
BASE_DIR = os.path.dirname(__file__)  #__file__python定义好的变量
DB_DIR = os.path.join(BASE_DIR,'db')
# print(BASE_DIR)
#print(DB_DIR)

username = input("输入用户名:")


def login():
    if exist_user(username):  #调用判断用户是否存在函数
        password = input("输入密码:")
        #检测用户名
        #用户存在则检查用户名，密码
        if password = xxx:
            load_user_info("xxx")
            return True
        else:
            return False
    else: #用户不存在则注册
        register(username)
        return True

login_result = login()
# #
def exist_user(username):
    user_info_file = os.path.join(DB_DIR,username)
    #print(user_info_file)
    if os.path.exists(user_info_file):
        print("存在")
        return True
    else:
        print("不存在")
        return False
exist_user('jfsu')
# def load_user_info(username):  # 加载用户信息
#     user_file = os.path.join(DB_DIR,username)
#     with open(user_file,'r') as f:
#         data = f.read()
#     user_clas = type(eval(data))   # f.read()输出为字符串，转化为字典 eval
#     return user_clas
# load_user_info('jfsu')

# def load_user_info(name):
#     #需要增加判断用户是否存在
#     u_file = os.path.join(DB_DIR,name)
#     f = open(u_file,'r')
#     data=f.read()
#     f.close()
#     u_info=eval(data)
#     return u_info
#
# load_user_info("han")

# def login():  # 认证登录
#
# def register(username):
# 	print("欢迎新用户 %s" % username)
#     while True:
#         password = input("输入新密码:")
#         npwd == len(password.strip())
#         if npwd > 0:
#             new_user(username,password)
#             #或者加载用户信息
#             load_user_info(username)
#             return True
#         else:
#             print("密码不能为空或空格，请重新输入")
#             continue

# def new_user(name,password): #把新用户信息存入文件
#     user = {
#         'password':password,
#         'balance':10000, # 可在函数头增加一个balance参数
#         'shopping_log':[]
#     }
#     new_user_file = os.path.join(DB_DIR,name)
#     print(new_user_file)
#     with open(new_user_file,'w') as f:
#         f.write(str(user))  #字典变成字符串，写入文件
# new_user('jfsu','123456')

# def show_product_list()
# 	print("展示商品编号,名称,价格")
# def user_choice():
# 	print("让用户输入选择的商品编号或者 q ,如果q就调用show_this_time_shopping_log并")
# def balance_enough():
# 	print("检查余额")
# def add_cart():
# 	print("放入购物车,并高亮显示,扣费,并调用日志信息")
# def show_shopping_log():
# 	print("显示用户购物日志")
# def save_user_status():
# 	print("用户信息存回文件")
# def shopping_log():
# 	print("添加到本次消费日志和用户信息日志中")
# def show_this_time_shop_log():
# def show_user_balance:
# 	print("显示余额并高亮显示")

if __name__ == '__main__':
    login()