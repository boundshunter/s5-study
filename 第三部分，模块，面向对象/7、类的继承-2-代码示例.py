#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

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

class Teacher(SchoolMember):
    '''
    老师类
    '''
    def __init__(self,name,age,sex,salary,course):
        SchoolMember.__init__(self,name,age,sex)
        self.salary = salary
        self.course = course
        self.teaching()
        SchoolMember.member += 1

    def teaching(self):
        print("Teacher [%s] teaching [%s]"%(self.name,self.course))

class Student(SchoolMember):
    '''
    学生类
    '''
    def __init__(self,name,age,sex,fee,course):
        #SchoolMember.__init__(self,name,age,sex)
        #第二种继承方法,此种继承方法将 类名和 self 写到一起
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

print(SchoolMember.member) # 打印人员数量

del s1
print(SchoolMember.member) # 打印人员数量
