#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

#新式类写法：
class SchoolMember(object):
    '''
    一个enroll方法，一个call（打印）方法，enroll（注册）每次自动调用
    '''
    member = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll() # enroll 每次自动调用
    def enroll(self):
        print("A new member [%s] has enrolled."%self.name)
    def call(self):
        print("***************[%s] info *****************"%self.name)
        for k,v in self.__dict__.items():
            print("\t",k,":",v)
        print("******************* END  ******************")
    def __del__(self):
        '''
        开出或者离职 ,member数字 减 1
        :return:
        '''
        print("离职人员或开出人员[%s]"%self.name)
        SchoolMember.member -= 1
class SchoolBranch(object):
    def open_branch(self,area):
        print("A new school branch in %s" % area )

class Teacher(SchoolMember):
    '''
    老师类
    '''
    def __init__(self,name,age,sex,salary,course):
        SchoolMember.__init__(self,name,age,sex)  # 老师继承 SchoolMember 类
        self.salary = salary
        self.course = course
        self.teaching()
        SchoolMember.member += 1

    def teaching(self):
        print("Teacher [%s] teaching [%s]"%(self.name,self.course))

class Student(SchoolMember,SchoolBranch):
    '''
    学生类
    '''
    def __init__(self,name,age,sex,fee,course):
        #SchoolMember.__init__(self,name,age,sex)  # 经典类写法
        #第二种继承方法,此种继承方法将 类名和 self 写到一起 ************新式类写法*****************
        super(Student,self).__init__(name,age,sex)
        self.fee = fee
        self.course = course
        self.amout = 0
        SchoolMember.member += 1
    def pay_amount(self,amount):
        print("Student [%s]'s fee is %s study [%s] need to pay [%s]"%(self.name,self.fee,self.course,amount))
        self.amount += amount

t1 = Teacher("jfsu",33,"M",30000,"PY-14")
s1 = Student('litao',25,'M',12000,"PY-15")
s2 = Student('wanglu',23,'F',11000,"PY-13")

t1.call()
s1.call()
s2.open_branch("SH")  # student 实现多继承，继承schoolmember和school branch
print(SchoolMember.member) # 打印人员数量

del s1
print(SchoolMember.member) # 打印人员数量

# 新式类 和 经典类 写法
# SchoolMember.__init__(self,name,age,sex)  # 经典类写法
#
# super(Student,self).__init__(name,age,sex) # 新式类写法

# 新式类 经典类 写法

# object 就是基类
class stu(object): # new style
    super
class stu: # 经典类

# 继承顺序  python3 和 python2 不同

python3 中查询术语； python3 中 广度查找 ，先找同级 （ 新式类和经典类 相同）

python2 中查询属于： python2 中 深度查询，每级找一个 （ python2 中经典用深度查询，新式类用广度查询）

何谓广度查询，深度查询
实例：
                     A
         B                       C
                     D

D 继承 B,C
B,C都继承A， B在左，C在右

广度查询继承关系，D先找自己，没有找B，在没有找C，在没有找A （ python3 经典类和新式类，python2 中新式类）

深度查询关系,D先找自己，没有找B，在没有找A，在没有找C ( python2 中 经典类)

