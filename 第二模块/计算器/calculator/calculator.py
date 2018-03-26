#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import re
import sys


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
        r = -(float(l[p-1]) * float(l[p+2]))
    # 定义 x 为 / 时 x 的下一位 是否为 -,如果 为 - 则 为负数
    elif x == '/' and l[p+1] != "-":
        r = float(l[p-1]) / float(l[p+1])
    elif x == '/' and l[p+1] == "-":
        r = -(float(l[p-1]) / float(l[p+2]))

    # 三个位置 计算后 ，删除 3个位置的元素
    del l[p-1],l[p-1],l[p-1]
    # 将 计算结果插入到删除位置
    l.insert(p-1,str(r))


def func(exps):
    '''
    函数计算主体，负责计算 只有加减乘除的运算
    :param exps:算式参数
    :return:返回计算结果
    '''
    #查找exps列表中，匹配数字 和数字. 的加减乘除，变成列表
    rel=re.findall('([\d\.]+|/|-|\+|\*)',exps)
    # print("打印初始列表",rel)
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
    '''
    负责算式的分解，循环将（）内的算式计算，最后将结果变成加减乘除运算在计算出结果
    :param exps:用户输入的算式
    :return:算式结果
    '''
    #定义提取 括号类元素的临时列表
    tmpex = []
    rlt = 0
    if '(' not in exps:
        rlt = func(exps)
        # print(rlt)
        return rlt

    else:
        # len(exps) 长度 从 0 开始
        for i in range(len(exps)):
            if exps[i] == '(':
                tmpex.append(i)
                # print("\033[41;1m ( 的位置:\033[0m",tmpex)
            elif exps[i] == ')':
                # print("\033[35;1m括号取值位置判断：\033[0m",(tmpex[len(tmpex)-1])+1,i)

                # len(tmpex) 长度, len(tmpex)-1 为列表tmpex最后一个元素，因为从0开始计算第一个元素；
                # (tmpex[len(tmpex)-1])+1 为最后一个元素'('下一位的位置，在 exps 中取值，i为第一个出现的')'

                subexpr = exps[tmpex[len(tmpex)-1]+1:i]  # 19-26
                # print("\033[42;1m子运算式\033[0m",subexpr)
                temp=func(subexpr)
                # print("\033[43;1m 存放临时结果 \033[0m",temp)
                # 初始化 exps 列表
                # len(tmpex-1) 为tmpex长度的最后一个元素 在exps 中 0到最后一个元素 )的位置，不取 )
                # 和 第一个最内层（）的字运算结果 str(temp)合并，在和exps的[i+1]位到最后一个元素合并
                # 作为新的 exps ,以此类推循环 ，每次循环计算 str(temp)的值
                exps = exps[0:tmpex[len(tmpex)-1]]+str(temp)+exps[i+1:]
                # print("第一段",exps[0:tmpex[len(tmpex)-1]])
                # print("第二段",str(temp))
                # print("第三段",exps[i+1:len(exps)+1])
                #  删除tmpex中最后一个元素
                tmpex.pop()
                return calculate(exps)

if __name__ == '__main__':
    while True:
        exps = input("\033[31;1m请输入您的要计算的算式：\033[0m")
        print("\033[35;1mcalculate程序运行计算结果为:%s \neval执行结果为:%s\033[0m"%(calculate(exps),eval(exps)))

        flag = input("按【q】退出程序，或者按任意键继续:")
        if flag == 'q':
            sys.exit("\033[42;1mExit the calculate program,Bye！\033[0m".center(50,'-'))
        else:
            continue

# exps = '2+10-((6-3)*2+(5-2)*3)'
# exps = '-100.5+40*5/2-3*2*2/4+9'
# exps = '1 - 2 * ( (60-30 +(-40/5+3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'