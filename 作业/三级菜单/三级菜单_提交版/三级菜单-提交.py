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
while exit_flag:
    print("欢迎访问大学查询系统".center(80,'*'))

    for index,key in enumerate(menu):
        #print(' '.join(['[',str(index),']',key]))
        print(index,key)

    # print(len(menu))

    choice1 = input("请输入您的选择编号:")
    if choice1.isdigit():
        choice1 = int(choice1)
        if choice1 >= 0 and choice1 < len(menu):
            # pass
            menu1 = menu.pop(key)
            print(menu1)
    else:
        exit_flat = False


