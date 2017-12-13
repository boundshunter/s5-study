#!/usr/bin/env python
# Author:summer_han

menu = {
    "吉林省":
        {
            "吉林市":{'东北电力','北华'},
            "长春市":{'吉林大学','东北师大'}
    },
    "黑龙江省":
        {
            "哈尔滨市":{'哈尔滨工业大学','哈尔滨工程大学'},
            "齐齐哈尔市":{'齐齐哈尔大学','齐齐哈尔医学院'}

    },
    "辽宁省":
        {
            "沈阳市":{"东北大学","辽宁大学"},
            "大连市":{"大连理工大学","大连海事大学"}
    }
}
exit_flag = True
menu_temp = []
while exit_flag:
    print("欢迎访问大学查询系统".center(80,'*'))

    # for key in menu:
    #     print(key,menu[key])
    for index,key in enumerate(menu):
        print(' '.join(['[',str(index),']',key]))
    #     menu_temp = menu.pop(key)
    # print(menu_temp)
    choice = input("请输入您的选择编号:")
    if choice.isdigit():
        choice = int(choice)
        while exit_flag:
            if choice >= 0 and choice < len(menu):
                menu=menu[key]
                print(menu)
    #             for index1,key1 in enumerate(menu.keys()):
    #
    #                 #print(' '.join(['\t','[',str(index1),']',key1]))
    #                 print(index1,key1)
    #                 i=input("--->")
    # else:
    #     pass
