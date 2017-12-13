#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
menu_data = {
    "吉林省":
        {
            "吉林市":{
                "江北区":{'东北电力','北华'},
            },
            "长春市":{
                "南关区":{'吉林大学','东北师大'}
            }
    },
    "黑龙江省":
        {
            "哈尔滨市":{
                "南岗区":{'哈尔滨工业大学','哈尔滨工程大学'},
            },
            "齐齐哈尔市":{
                "龙沙区":{'齐齐哈尔大学','齐齐哈尔医学院'}
            }

    },
    "辽宁省":
        {
            "沈阳市":{
                "皇姑区":{"东北大学","辽宁大学"},
            },
            "大连市":{
                "甘井子":{"大连理工大学","大连海事大学"}
            }
        }
}
import sys
import os
BASE_DIR = os.path.dirname(__file__)
DICT_DIR = os.path.join(BASE_DIR,'dict.txt')

if os.path.exists(DICT_DIR):
    os.remove(DICT_DIR)

# 字典以字符串形式写入文件
with open('dict.txt','a',encoding="utf-8") as f:
    f.write(str(menu_data))

# 读出字典信息
with open('dict.txt','r',encoding="utf-8") as f1:
    menu = eval(f1.read())

# 开始循环
while True:
    for i in menu:
        print(i)
    choice1 = input("请输入选择进一层,按q退出--->:") # 进入第一层

    if choice1 in menu: # 判断是否在字典key中
        while True:
            for i1 in menu[choice1]:
                print(i1)
            choice2 = input("请输入选择进二层，按q退出，按b返回上一级--->:")  # 进入第二层

            if choice2 in menu[choice1]: # 判断输入是否在 第二层key中
                while True:
                    for i2 in menu[choice1][choice2]:
                        print(i2)
                    choice3 = input("请输入选择三层，按q退出，按b返回上一级--->:") # 进入第三层

                    if choice3 in menu[choice1][choice2]:  # 判断第三层是否在key中
                        while True:
                            for i4 in menu[choice1][choice2][choice3]:
                                print(i4)
                            choice4 = input("已经是最后一层，按q退出，按b返回上一级--->:")  # 最后一层提示信息

                            if choice4 not in 'bq':
                                print("按q退出，按b返回上一级")
                                continue
                            elif choice4 == 'b':
                                print("最底层，返回上一级")
                                break
                            elif choice4 == 'q':
                                print("退出程序")
                                sys.exit()
                            else:
                                print("输入错误，退出程序")
                                sys.exit()

                    elif choice3 == 'b':
                        print("第三层，返回上一层")
                        break
                    elif choice3 == 'q':
                        print("退出程序")
                        sys.exit()
                    else:
                        print("输入错误，退出程序")
                        sys.exit()
            elif choice2 == 'b':
                print("已经是最上层，无法返回，请选择省份！")
                break
            elif choice2 == 'q':
                print("退出程序")
                sys.exit()
            else:
                print("输入错误，请重新输入")
                sys.exit()
    elif choice1 == 'b':
        print("已经是最上层，无法返回，请选择省份！")
        break
    elif choice1 == 'q':
        print("退出程序")
        sys.exit()
    else:
        print("输入错误，请重新输入")
        sys.exit()

os.remove('dict.txt')  #删除最初生成字典