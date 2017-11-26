#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
menu = {
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
exit_flag = False
menu_temp = {}
while True:
    print("进入一级菜单".center(60,'-'))
    for index1,key1 in enumerate(menu.keys(),1):
        print(index1,key1)
        menu_temp[index1] = key1
    #print(type(menu_temp.keys()))

    choice1 = input("LEVEL_1,输入'b'返回，输入'q'退出--->:")
    for L1 in menu_temp.keys():

        print(type(L1))
        # if choice1 in str(L1):
        #     print(menu_temp.values())
        #     # print(menu[menu_temp[choice1]])
        # elif choice1 == 'q':
        #     exit_flag= True
        # elif choice1 == 'b':
        #     print("当前为顶级菜单，无法返回，请进入下一级")
        # else:
        #     print("输入错误，退出程序")
        #     sys.exit()
# import sys
# dict_key = {}
# def menu1():
#     print('进入1级菜单'.center(70,'-'))
#     for index1,key1 in enumerate(menu.keys(),1):   # 遍历一级菜单,index从1开始
#         print(index1,key1)
#         dict_key[str(index1)]= key1  #初始化 dict_key 字典
#     # print("L1->:",dict_key)
#     choose = input("输入编号选择，输入b返回上一级菜单，输入q退出菜单:")
#     if choose == 'q':
#         #str.lower(choose)
#         quit()
#     elif choose == 'b':
#         print("顶层菜单无法返回，请选择数字进入下一级")
#     elif dict_key.get(choose):
#         menu2(dict_key[choose])
#     else:
#         menu1()
#         print("输入错误，重新输入")
#
#
# def menu2(choose1):
#     print("进入2级菜单".center(60,'-'))
#     for index2,key2 in enumerate(menu[choose1].keys(),1):
#         print(index2,key2)
#         dict_key[str(index2)] = key2
#     # print("L2->:",dict_key)
#     choose2 = input("输入编号选择，输入b返回上一级菜单，输入q退出菜单:")
#     if choose1 == 'q':
#         sys.exit()
#     elif choose1 == 'b':
#         menu1()
#     elif dict_key.get(choose2):
#         menu3(choose1,dict_key[choose2])
#     else:
#         print("输入错误，重新输入")
#
# def menu3(choose1,choose2):
#     print("进入3级菜单".center(60,'-'))
#     print(type(menu[choose1][choose2]))
#     for index3,key3 in enumerate(menu[choose1][choose2],1):
#         print(index3,key3)
#         dict_key[str(index3)] = key3
#     # print("L3->:",dict_key)
#     choose3 = input("输入编号选择，输入b返回上一级菜单，输入q退出菜单:")
#     if choose3 == 'q':
#         sys.exit()
#     elif choose3 == 'b':
#         menu2(choose1)
#     elif dict_key.get(choose3):
#         menu4(choose1,choose2,dict_key[choose3])
#     else:
#         print("输入错误，重新输入")
#
# def menu4(choose1,choose2,choose3):
#     for index4,key4 in enumerate(menu[choose1][choose2][choose3],1):
#         print(index4,key4)
#     print(type(menu[choose1][choose2][choose3]))
#
#
#
# while True:
#     if cls_type == set:
#         print("L4")
#     else:
#         menu1()









