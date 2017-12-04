__author__ = 'sujunfeng'

import os
import sys

BASE_DIR = os.path.dirname(__file__)  # __file__python定义好的变量
DB_DIR = os.path.join(BASE_DIR,'user_info.txt')

#初始化 文件
# salary_list = {
#     'Alex':100000,
#     'Rain':80000,
#     'Egon':50000,
#     'Yuan':30000
# }
# with open('user_info.txt','w',encoding="utf-8") as f_init:
#     f_init.write(str(salary_list))

change_list = ['查询员工工资','修改员工工资','增加新员工记录','退出']

with open(DB_DIR,'r',encoding="utf-8") as f:
    info = eval(f.read())
# print(info['Alex'])

def request_list(): # 定义显示功能列表函数
    for i in enumerate((change_list),1):
        print(i[0],i[1])

def select_staff_info(username):  # 定义查询用户名信息函数
    salary = info[username]
    output = input("%s 的工资是: %s  " % (username,salary))
    return output

def alter_staff_info(username,salary): # 修改员工姓名函数
    info[username] = salary
    with open(DB_DIR,'w',encoding='utf-8') as f_alter:
        f_alter.write(str(info))
    print("修改成功")

def add_staff_info(username,salary):
    info.setdefault(username,salary) # 增加一个字典值
    with open(DB_DIR,'w',encoding="utf-8") as f_add:
        f_add.write(str(info))
    print("增加成功")

def exit_system():
    print("退出程序")
    sys.exit()


def login(): # 定义主体函数
    request_list()  # 调用显示功能列表函数
    while True:
        choice = input(">>:")
        if choice == '1':
            exit_flag = False
            while not exit_flag:
                username = input("输入要查询的员工姓名（例如Alex）:")
                if username in info:
                    select_staff_info(username)
                    print("\r")
                    login()
                    continue
                else:
                    print("您的用户名输入错误，请重新输入:")
                    continue
        elif choice == '2':
            while True:
                count = input("请输入要修改的员工姓名和工资，用空格分隔(例如：Alex 10) : ").split()
                if len(count) == 2:
                    #username,salary = input("请输入要修改的员工姓名和工资，用空格分隔(例如：Alex 10) : ").split()
                    username = count[0]
                    salary = count[1]
                    if username in info:
                        alter_staff_info(username,salary)
                        print("\r")
                        login()
                    else:
                        print("您的用户不存在，重新输入！")
                        continue
                else:
                    print("您输入的参数不对，请重新输入!")
                    continue

        elif choice == '3':
            while True:
                input_args = input("请输入要增加的员工姓名，工资，用空格分隔符(例如：Eric 100000) :").split()
                if len(input_args) == 2:
                    username = input_args[0]
                    salary = input_args[1]
                    # print(username)
                    # print(salary)
                    if username not in info:
                        add_staff_info(username,salary)
                        login()
                    else:
                        print("您输入的用户存在，请使用其他用户名!")
                        continue
                else:
                    print("您输入参数个数有误，请重新输入！")
                    continue
        elif choice == '4':
            exit_system()

        else:
            print("您的选择有误，请重新选择")
            login()

if __name__ == '__main__':
    login()






