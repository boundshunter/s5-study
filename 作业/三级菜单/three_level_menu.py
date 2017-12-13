#!/usr/bin/env python
# _Author_: summerhan Su
import sys

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

menu_high = menu
menu_middle = []
menu_low = []

while True:
    for index,key in enumerate(menu_high):

        if type(menu_high) == dict:
            #''.join() 固定用法''内可以说明分隔符，默认无分隔符例如' '一个空格,menu_middle有几个元素，就在组合后前面显示几个>
            print(' '.join(['>'*len(menu_middle),'[',str(index),']',key]))
            # input("--->")

        else:
            print(' '.join(['\t'*len(menu_middle),'[',str(index),']',key]))

        menu_low.append(key)
    #print(menu_low)

    choose = input("请输入选择编号>>>:")

    if choose.isdigit():

        if type(menu_high) == dict:
            idx = int(choose)

            if idx >= 0 and idx < len(menu_low):

                k1 = menu_low[idx]
                menu_middle.append(menu_high)
                menu_high = menu_high[key]   #进入选择数字对应字典key的下一层
                #print(k1)
            else:
                print("输入数字错误，请重新输入！")

        else:
            print("已经到最后一级"'\n'
                  "请按[ b ]返回上级菜单" '\n' ,
                  "按 [ q ] 退出")

    elif choose == 'b':

        if len(menu_middle) > 0:
             menu_high = menu_middle.pop()
        else:
            print("已回退到省份，请选择数字项进入菜单或者按[ q ]退出程序")

    elif choose == 'q':
        print("退出菜单".center(80,'*'))
        sys.exit()

    else:
        print("输入错误，重新输入")
