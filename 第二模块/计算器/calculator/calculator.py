#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
# 参考 https://www.cnblogs.com/Wxtrkbc/p/5453349.html

import re

# expression = '-15+60*3/2-3*5*6/7+9'
# expression = "1+(2+(3*(4+5))+6)"
# l = re.findall('[\d\.]+|\+|-|\*|/',expression) # \d\.匹配任意整数或者小数，\+ \* 匹配+ 和* - / 不需要转义
# print(l) # 取出所有符号 放入列表 l

def mult_div(l,x):                                   # 定义最小乘除法单元，l为列表  x 为 * 或 /
    a = l.index(x)                                   # 获取 * 运算符 位置

    if x == "*" and l[a+1] != "-":                                     # 如果是 乘法
        rlt = float(l[a-1]) * float(l[a+1])          # 获取 乘法运算结果 rlt = 1 * 2
    elif x == "/" and l[a+1] != "-":
        rlt = float(l[a-1]) / float(l[a+1])
    elif x == "*" and l[a+1] == "-":
        rlt = -(float(l[a-1]) * float(l[a+2]))
    elif x == "/" and l[a+1] == "-":
        rlt = -(float(l[a-1]) / float(l[a+2]))          # 否则获取 除法运算结果

    del l[a-1],l[a-1],l[a-1]                         # 符号前后和运算符共占用 3个位置，左边数字为第一个位置，删除一个元素，后面元素自动提前一个位置
                                                     # 连续删除 3个元素 即 1 * 2 三个元素都删除
    l.insert(a-1,str(rlt))                                # 删除位置 替换为 三个元素运算结果 ，插入列表中
    # print(l)                                         # 打印列表查看结果

# mult_div(l,'*')

def func(args):
    # print("args:",args)
    # print(l)
    sum = 0
    while l:
        if '*' in l and '/' not in l:             # 如果只有乘 没有 除
            mult_div(l,'*')

        elif '/' in l and '*' not in l:           #如果 只有除 没有 乘
            mult_div(l,'/')

        elif '*' in l and '/' in l:               # 如果 既有 乘 又有 除
            mul = l.index('*')
            div = l.index('/')

            if mul < div:                          # 乘的位置 在 除之前
                mult_div(l,'*')                    # 先执行乘
            else:
                mult_div(l,'/')                    # 除的位置在乘之前，先执行除

        else:                                     # 计算 加减法
            if l[0] == '-':                       # 判断 列表第一个元素是否为 - （负号）
                l[0] = l[0]+l[1]                  # 将第一个元素 替换为 第一个元素和第二个元素合并后结果
                del l[1]                          # 然后将第二个 无用 元素 删除
            # print("----------",l)                              # 打印 合并首位负数后的列表
            sum += float(l[0])                    # 将存在的负数合并后只剩下 加减法运算
            # print("0位负号的算式:",sum)
            for i in range(1,len(l),2):         # l列表内 从第一个元素到 最后一个元素 遍历 步长为2 取运算符 i 位置
                if l[i] == '+' and l[i+1] != "-":
                    # print("打印符号：",l[i])
                    sum += float(l[i+1])
                    # print(sum)
                elif l[i] == "+" and l[i+1] == "-": # 判断 i+1 是否为 -
                    sum -= float(l[i+2])             # 减法
                    # print("+挨着-:",l[i])
                elif l[i] == "-" and l[i+1] != "-":
                    sum -= float(l[i+1])
                    # print("+不挨着-:",l[i])
                elif l[i] == "-" and l[i+1] == "-":
                    sum += float(l[i+2])
            break
    # print(sum)
    return sum

def calc(args):

    expression=args
    pos = []
    rlt = 0
    while True:
        if '(' not in expression:

            rlt = func(expression)
            # print("not )")
            print(rlt)
            # return rlt
            return rlt

        else:
            print("存在 ()")
            for i in range(len(expression)):
                if expression[i] == '(':
                    pos.append(i)                    # 记录 '(' 出现的位置，并记录到新的列表 pos中
                    print(pos)

                elif expression[i] == ')':
                    rlt_tmp = 0                      # 初始化临时结果，用于将临时的结果记录
                    sub = expression[pos[-1]+1:i]    # 取pos最后一个元素'('位置 的下一位 pos[-1]+1
                    # sub = expression[pos[len(pos)-1]+1:i]
                    print(sub)
                    rlt_tmp = func(sub)
                    expression = expression[0:pos[-1]-1]+str(rlt_tmp)+expression[i+1:-1]
                                                     # 将所有（）内算式替换为sub的值，然后将(前的元素，替换后元素，
                                                     #）后元素合并为新的列表，赋值给 expression
                    print(expression)
                    pos.pop()
                    # print(rlt_tmp)
            return rlt


if __name__ == '__main__':
    args=input("请输入您要计算的算式>>:")
    l = re.findall('[\d\.]+|\+|-|\*|/',args)
    calc(args)



