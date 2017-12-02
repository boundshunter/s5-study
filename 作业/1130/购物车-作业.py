# __Author__ : sujunfeng

shopping_list=[
    ("Iphone X",8999),
    ("Mac pro",17999),
    ("Bike",999),
    ("Balance car",1999),
    ("Book",59),
    ("IWatch",3999)
]

# user_info_dict = {
#     'jfsu':{
#         'password':'abc123!',
#         'salary':30000
#     },
#     'mmm':{
#         'password':'123123',
#         'salary':50000
#     }
# }

# with open('user_info_list.txt','w',encoding="utf-8") as f_init:
#     f_init.write(str(user_info_dict))

# new_user_info = {'hanhan':{'password':'abc123','salary':10000000}}

# user_new_dict = dict(user_info_dict,**new_user_info) # 新用户字典和老用户字典合并
# print(user_new_dict)

#new_user_info = {'user_login':{'password''':'new_user_password'','salary':'new_user_salary'}}

with open("user_info_list.txt",'r') as f:
    info=f.read()
    user_info_dict = eval(info)
print(user_info_dict)



for menu in shopping_list:
    #print(menu[1][1])
    print(shopping_list.index(menu),menu)

user_login = input("请输入您的用户名:")


if user_login in user_info_dict:
    print(user_login)
else:
    print("您的用户不存在，需要注册!")
    new_user_password = input("请输入您的密码:")
    exit_flat = False
    while not exit_flat:
        if new_user_password.strip() != "":
            new_user_salary = input("请冲入您的金额:")
            if new_user_salary.isdigit():
                new_user_salary=int(new_user_salary)
                new_user_info = {user_login:{'password':new_user_password,'salary':new_user_salary}} #合并到 user_info_dict
                print(new_user_info)
                user_new_dict = dict(user_info_dict,**new_user_info)    #合并新用户字典到 所有用户字典

                with open('user_info_list.txt','w',encoding="utf-8") as f_init:
                    user_all_dict = f_init.write(str(user_new_dict)) #所有用户字典初始化到文件

                #print(user_all_dict)
                print('登录成功，欢迎您 %s '% user_login)
                break
            else:
                print("您的输入不正确，请输入充值金额的数字！")
                break
        else:
            print('您的密码输入不符合要求，请重新输入，或者退出程序，是否退出？')
            logout = input("请输入您的选择Y/N")
            if logout == 'y':
                break

