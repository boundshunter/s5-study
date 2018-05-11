#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

1、什么是面向对象：
    - 以前是使用函数
    - 类 + 对象

2、什么是类，什么是对象，什么关系？
    class 类:
        def 函数1(self):
            pass
        def 函数2(self)：
            pass

    对象：生成对象的过程也叫实例化
    obj = 类()
    obj.函数1()

3、什么时候选择函数式编程，什么时候选择面向对象编程
    - 函数式编程简单
    - 面向对象复杂

    什么场景适用 面向对象:
    3个场景:
    登录一台服务器后：
    1、先帮我执行一个命令   （ 1、连上服务器，2、执行命令 3、关闭）
    2、先帮我上传一个文件     1、连上服务器，2、执行命令 3、关闭）
    3、先帮我上传一个文件，在执行一个命令  1、连上服务器，2、上传文件 3、执行命令 4、关闭）

面向对象应用场景示例：
·如果使用函数式 编程
·模板类（根据一个模板创建某些东西）
·对个函数需要传入共同的参数时，使用面向对象

class SSH:
    def __index__(self,IP,host,pwd):
        self.ip = IP
        ...
    def conn(self):
        # 去创建连接
        self.conn = 和服务器创建连接对象()

    def close(self):
        # 关闭
        self.conn.关闭

    def cmd(self): # 内部调用conn方法
        self.conn  执行命令
    def upload(self): # 内部调用conn方法
        self.conn   使用上传文件

# 一次连接调用，可以执行多种操作方式
obj = SSH('IP','host','pasw')
obj.conn()
obj.cmd()
obj.upload()
obj.xxx
obj.close()

# 函数式编程，每次都需要重新建立一次连接

# 对个函数，传递参数示例：
def f1(name1,name2,name3,arg1):

def f2(name1,name2,name3,arg1,arg2):

def f3(name1,name2,name3,arg1,arg2,arg3):

上面3个函数都需要传入共同的参数，避免对此传入参数，使用面向对象

class Foo:
    def __init__(self,name1,name2,name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3

    def f1(self,arg1):
        self.name1
        self.name2
        self.name3
    def f2(self,arg1,arg2):
        self.name1
        self.name2
        self.name3

    def f3(self,arg1,arg2,arg3):
        ...
#示例化，生成对象
obj = Foo(1,2,3)
# 只需要传入不同的参数
obj.f1(arg1)
obj.f2(arg1,arg2)
obj.f3(arg1,arg2,arg3)


##########################################
4、self 就是调用当前方法的对象
    # 如果 每个对象里面都有一个共同的值，就可以设置为公有属性
    class Foo:
        # 静态字段
        # 公有属性
        country = "china" # 只保存一次

        def __init__(self,name,count):
            # 普通字段
            # 普通属性
            self.NAME = name
            self.COUNT =count
            # self.country = "china" # 放到这，每个对象都要调用一次
        def bar(self):
            pass
    obj1 = Foo("河南",100000000)
    obj1.bar()
    obj2 = Foo("山东",50000000)
    obj2.bar()

5、封装 属性也可以成为字段
    ·类中封装了字段和方法
    ·对象封装了：普通属性（字段）的值

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


