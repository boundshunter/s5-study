#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import re
def md(l,x):
    a = l.index(x)
    if x == '*' and l[a + 1] != '-':
        k = float(l[a - 1]) * float(l[a + 1])
    elif x == '/' and l[a + 1] != '-':
        k = float(l[a - 1]) / float(l[a + 1])
    elif x == '*' and l[a + 1] == '-':
        k = -(float(l[a - 1]) * float(l[a + 2]))
    elif x == '/' and l[a + 1] == '-':
        k = -(float(l[a - 1]) / float(l[a + 2]))
    del l[a - 1], l[a - 1], l[a - 1]
    l.insert(a - 1, str(k))
    return l

def fun(s):
    l = re.findall('([\d\.]+|/|-|\+|\*)',s)
    sum=0
    while 1:
        if '*' in l and '/' not in l:
            md(l, '*')
        elif '*' not in l and '/' in l:
            md(l, '/')
        elif '*' in l and '/' in l:
            a = l.index('*')
            b = l.index('/')
            if a < b:
                md(l, '*')
            else:
                md(l, '/')
        else:
            if l[0]=='-':
                l[0]=l[0]+l[1]
                del l[1]
            sum += float(l[0])
            for i in range(1, len(l), 2):
                if l[i] == '+' and l[i + 1] != '-':
                    sum += float(l[i + 1])
                elif l[i] == '+' and l[i + 1] == '-':
                    sum -= float(l[i + 2])
                elif l[i] == '-' and l[i + 1] == '-':
                    sum += float(l[i + 2])
                elif l[i] == '-' and l[i + 1] != '-':
                    sum -= float(l[i + 1])
            break
    return sum
def calculate(expression):
    ex=[]
    ans=0
    if '(' not in expression:
        ans=fun(expression)
        return ans
    for i in range(len(expression)):
        if expression[i]=='(':
            ex.append(i) #ex=[6,7]
            print("\033[42;1m   (   \033[0m",ex)
        elif expression[i]==')': #14
            # temp=0
            sub=expression[ex[len(ex)-1]+1:i]
            print("\033[41;1m sub  \033[0m",sub)
            print(expression)
            temp=fun(sub)
            print("\033[43;1m 存放临时结果 \033[0m",temp)
            expression=expression[0:ex[len(ex)-1]]+str(temp)+expression[i+1:len(expression)+1]
            ex.pop()
            return calculate(expression)

s='1+2+((3+5)*3+(5-3)*2)-10'
print(calculate(s))