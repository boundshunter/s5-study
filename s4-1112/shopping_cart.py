#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
product_list=[
    ("Iphone X",8999),
    ("Mac pro",17999),
    ("Bike",999),
    ("Balance car",1999),
    ("Book",59),
    ("IWatch",3999)
]
shopping_list = []
salary=input("Please input your balance: ")
if salary.isdigit():
    salary = int(salary)
    #else:
    # print("Your input in not a number，please input a number")
        #方法1：显示下标和列表
       # for menu in shopping_list:
         # print(shopping_list.index(menu),menu)
        #方法2：enumerate 显示列表元素index下标
    while True:
        for index,menu in enumerate(product_list): #取商品下标编号和商品列表
            print(index,menu)
        user_choice = input("请输入您要购买的商品编号:")
        if user_choice.isdigit(): # 判断输入是否为数字
            user_choice = int(user_choice) #转换为整形
            if user_choice <= len(product_list) and user_choice >= 0: #数字在商品列表长度范围内
                product_item=product_list[user_choice] #定义商品 选项
                #print(product_item)
                if product_item[1] < salary: #如果商品选项对应金额 小于 余额
                    salary -= product_item[1] #余额 = 余额 - 商品金额
                    shopping_list.append(product_item) #购物车列表 增加 购买商品
                    #print()
                else: #买不起
                    print("您的余额只剩[%s]请尽快充值." % (salary))
            else: #选错编号
                print("商品编号(%s)不存在，请重新输入数字编号" % (user_choice))
        elif user_choice == 'q':
            print("-----------shopping list---------------")
            for product in shopping_list:
                print(product)
            print("您当前余额为 (%s):" % salary)
            exit()
        else:
            print("Invild option!")
else:
    print("Please input number ,not string")
