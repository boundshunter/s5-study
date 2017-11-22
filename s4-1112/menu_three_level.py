#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
data = {
    '北京':{
        "海淀":{
            "中关村":{"东奥","新东方"},
            "公主坟":{"翠微","mall"},
            "四季青":{"四季青医院","金源"},
        },
        "朝阳":{
            "望京":{"奔驰","陌陌"},
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
             },
    },
    "山东":{
        "青岛":{
            "市南区":{"海尔","青岛啤酒"},
        },
        "济南":{
            "市中区":{"大明湖","趵突泉"},
        },
    },
}
exit_flag= False

while not exit_flag:
    for L1 in data:
        print(L1)
    choice1 = input("进入层 1 >>>:")
    if choice1 in data:
        while not exit_flag:
        #print(choice1)
            for L2 in data[choice1]:
                print("\t",L2)
            choice2 = input("进入层 2 >>>:")
            if choice2 in data[choice1]:
                while not exit_flag:
                    for L3 in data[choice1][choice2]:
                        print("\t",L3)
                    choice3 = input("进入层 3 >>>:")
                    while not exit_flag:
                        if choice3 in data[choice1][choice2]:
                            for L4 in data[choice1][choice2][choice3]:
                                print("\t\t",L4)
                            choice4 = input("最后一层了，按b返回上层>>>:")
                            if choice4 == 'b':
                                pass #占位符，不做任何操作
                            elif choice4 == 'q':
                                 exit_flag = True
                        if choice3 == 'b':
                            break
                        elif choice3 == 'q':
                            exit_flag = True
            if choice2 == 'b':
                    break
            elif choice2 == 'q':
                    exit_flat = True
集合