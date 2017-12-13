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

user_info_list = {}

shopping_list = []
salary=input("Please input your balance:" )

if salary.isdigit():
    salary = int(salary)

    while True:
        for menu in product_list:
            print(product_list.index(menu),menu)
        user_choice = input("please input your shopping number:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                product_item = product_list[user_choice]
                print(product_item)
                if salary >= product_item[1]:   #买得起
                    salary = salary - product_item[1]
                    shopping_list.append(product_item)
                    print("Adding %s into your shopping cart,your current balance is %s" % (product_item[0],salary))
                else:
                    print("\033[42;1m余额不足，您的余额为[%s]\033[0m" % salary )
            else:
                print("您输入的数字超出范围，请选择商品范围为0-[%s]" % len(product_list))
        elif user_choice == 'q':
            print("\033[42;1m----------shopping list---------------\033[0m")
            for p in shopping_list:
                print(p)
            print("Your balance is \033[42;1m %s \033[0m" % salary)
            exit()

        else:
            print("Invalid option.")

c = dict.fromkeys(['5','test1'],['6','test2'])
print(c)