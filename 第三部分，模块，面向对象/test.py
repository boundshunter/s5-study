#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
class F1:
    def __init__(self,n):
        self.N = n
        print("F1")
class F2:
    def __init__(self,arg1):
        self.a = arg1
        print('F2')
class F3:
    def __init__(self,arg2):
        self.a = arg2
        print("F3")

o1 = F1('alex')
o2 = F2(o1)
o3 = F3(o2)
###### 输出 alex ######
o3 = F3(o2)
o3.b = o2

o2.a = o1  # o3.b.a = o1

o1.N = 'alex' # o3.b.a.N = alex
##########################

# 继承
# 示例：

class F1:
    def __init__(self):
        print(F1)
    def a1(self):
        print("F1a1")
    def a2(self):
        print("F1a2")

class F2(F1):
    def __init__(self):
        print(F1)
    def a1(self):
        self.a2
        print("F2a1")
    def a2(self):
        print("F2a2")
class F3(F2):
    def __init__(self):
        print(F1)
    # def a1(self):
    #     print("F3a1")
    def a2(self):
        print("F3a2")

obj = F3()
obj.a1()
#输出结果
# F3a2,F2a1
#分析：
obj.a1()，首先 在F3里寻找a1
F3里面不存在a1
然后去父类F2中寻找a1
F2中存在a1
F2的a1中 调用 self.a2

self 就是F3 本身，self.a2 = F3.a2
回到F3中寻找a2，F3中存在a2，输出F3a2

在继续在F2的a1中执行，打印print("F2a1")
所以又输出 F2a1

所以最终结果 F3a2,F2a1

#######################################################
方法：
    ·普通方法（保存在类中，调用者对象至少有一个self参数,有函数封装）
    ·静态方法（保存在类中，调用者是类，无需对象，不需要封装，可以有任意个参数） 类似于函数式编程

静态方法示例：
class Foo:
    @staticmethod # 声明为静态访问，不需要函数封装，
    def a1(b1,b2,b3.....):
        print('alex')

# 调用类似函数调用
# 静态方法调用之前不需要创建对象
Foo.a1(b1,b2,b3......)
将静态方法 等同于 函数式编程



最后我们总结出领域建模的三字经方法:找名词、加属性、连关系

