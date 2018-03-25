#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han


import re

def mult_div(l,x):
    '''
    定义最小 乘法和除法单元 并计算后 只剩下 加减法 ,l 为 正则转换后的 list, x 代表 * 或者 /
    :param l:
    :param x:
    :return:
    '''
    p = l.index(x)
    # print(p,l)
    # 定义 x 为 * 时 x 的下一位 是否为 -,如果 为 - 则 为负数
    if x == '*' and l[p+1] != "-":
        r = float(l[p-1]) * float(l[p+1])
    elif x == '*' and l[p+1] == "-":
        r = -(float(l[p-1]) * float(l[p+1]))
    # 定义 x 为 / 时 x 的下一位 是否为 -,如果 为 - 则 为负数
    elif x == '/' and l[p+1] != "-":
        r = float(l[p-1]) / float(l[p+1])
    elif x == '/' and l[p+1] == "-":
        r = -(float(l[p-1]) / float(l[p+1]))

    # 三个位置 计算后 ，删除 3个位置的元素
    del l[p-1],l[p-1],l[p-1]
    # 将 计算结果插入到删除位置
    l.insert(p-1,str(r))
    # 打印计算后的列表
    # print(l)


def func(exps):
    rel=re.findall('([\d\.]+|/|-|\+|\*)',exps)
    print("打印初始列表",rel)
    # 当rel为真时
    while True:
        #  既有乘法又有除法运算符时，判断乘除法运算符位置，位置小的优先计算
        if '*' in rel and '/' in rel:
            pos_A = rel.index('*')
            pos_B = rel.index('/')
            #  判断 乘除法运算符 位置
            if pos_A < pos_B:
                mult_div(rel,'*')
                # print(rel) # 打印rel 对比 list
            else:
                mult_div(rel,'/')
        #  只有 乘法 没有 除法
        elif '*' in rel and '/' not in rel:
            mult_div(rel,'*')
        # 只有 除法 没有 乘法
        elif '*' not in rel and '/' in rel:
            mult_div(rel,'/')

        else:
            #  初始化 运算结果为 0
            sum = 0
            #  判断列表第一个元素是否为 '-' 如果为 '-' 则合并 前两个元素，并且删除第二个元素 rel[1],保留合并后的元素
            if rel[0] == '-':
                rel[0] = rel[0] + rel[1]
                # 删除合并后的无用 元素
                del rel[1]
                # 打印结果查看列表元素是否正确
                # print(rel)
            #  初始化运算结果 为列表第一个元素的值
            sum += float(rel[0])
            # print('---------------',sum)

            #  判断元素符号,范围为1到列表最大长度，步长为2
            for i in  range(1,len(rel),2):
                #  打印 符号 （+ -）
                # print(rel[i])

                # 判断 + 后后面是否是'-',如果不是'-' 则 sum结果为 加下一位
                if rel[i] == '+' and rel[i+1] != '-':
                    sum += float(rel[i+1])
                # 判断 + 后面是否为 '-',如果是'-',则 sum 结果为 - i+2位 （i+1位是'-')
                elif rel[i] == '+' and rel[i+1] == '-':
                    sum -= float(rel[i+2])
                # 判断 - 后后面是否是'-',如果不是'-' 则 sum结果为 减下一位
                elif rel[i] == '-' and rel[i+1] != '-':
                    sum -= float(rel[i+1])
                # 判断 - 后后面是否是'-',如果是'-' 则 sum结果为 加下一位
                elif rel[i] == '-' and rel[i+1] == '-':
                    sum += float(rel[i+2])
            # print(sum)
            return sum

# expression = '-100.5+40*5/2-3*2*2/4+9'

def calculate(exps):
    tmpex = []
    rlt = 0
    if '(' not in exps:
        rlt = func(exps)
        print(rlt)
        return rlt

    else:
        for i in range(len(exps)):
            if exps[i] == '(':
                print(i,exps[i+1])
                tmpex.append(i)
                print(tmpex)
            elif exps[i] == ')':
                # print("tmpex 长度:%s,tmpex元素'('位置 :%s"  %  (len(tmpex),tmpex[len(tmpex)-1]))
                # subexpr = exps[tmpex[len(tmpex)]:i]
                print("tmpex 长度:%s,tmpex元素'('位置 :%s"
                      % (len(tmpex),tmpex[len(tmpex)-1]),exps[tmpex[len(tmpex)-1]+1:i])

exps = '1 - 2 * ( (60-30 +(-40/5+3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

calculate(exps)



