#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:苏俊峰

#1、模拟登录
#2、用户输入账户，密码
#3、用户密码输入错误，三次后锁定

#4、没有的用户可以注册，加入字典,写入文件
'''
f=open("u_dict.txt",'r')
user_info=f.read()
f.close()
user_ls=user_info.split('\n')
user_dict={}
#获取 用户字典
for item in user_ls:
    item_list = item.split("\t")
    #print(item_list[0],item_list[1])
    #user_dict[item_list[0]]=item_list[1] #两种初始化方法 方法1
    user_dict.setdefault(item_list[0],item_list[1]) #方法2
#print(user_dict)

#获取锁定用户信息
lock_f=open("lock_f.txt",'r')
lock_info=lock_f.read()
lock_f.close()

lock_list=lock_info.split()
#print(lock_list)
#print(type(lock_list))
#lock_list = [] #初始化一个列表，列表可以从db中读取
name=input("登录用户--->:")
def login():
    if name not in lock_list: # 判断输入是否在 锁定列表
        done = False   #定义初始化值
        while not done:
            if name in user_dict.keys(): #判断用户名是否在字典中 ，如果在就执行下面
                pwd=input("登录密码--->:")
                password=user_dict.get(name)
                if pwd == password: #判断密码是否正确
                    print("welcome back,dear %s" % name)
                    done = True #密码正确，退出
                else: #密码不正确
                    count=0 #初始化 输入次数
                    while count<2: #当次数 在3次以内，从0开始计数
                        print("密码错了，请重新输入，还可以尝试 %s 次" % (3 - count))
                        pwd=input("password--->:")
                        count+=1 #循环 次数 +1
                        if count >= 2:  #次数大于3次
                            lock_list.append(name) # 用户加入锁定列表
                            #写入锁定文件
                            lock_open=open("lock_f.txt",'a')
                            #print(lock_list)
                            lock_open.write(name)
                            lock_open.write('\n')
                            lock_open.close()

                        done=True #退出
            else: #用户不存在 ，准许注册，写入dict
                print("不存在的用户名-- %s --,请注册！" % name)
                register_name = input("register_name:")
                register_pwd = input("register_pwd:")
                #user_dict.setdefault(register_name,register_pwd)
                #把最后字典写入文件
                #字典转换列表
                u_info=open("u_dict.txt",'r')
                u_get=u_info.read()
                u_info.close()
                u_list=u_get.split()
                print(u_list)
                list.append(register_name,register_pwd)
                #print()
                #print(user_dict)
                done = True
        else:
            done = True
    else: #判断名字在锁定列表，提示用户联系管理员
        print("账户被锁定，请联系管理员 qq:1234567789")
        exit
if __name__ == '__main__':
    login()
'''

u_info=open("u_dict.txt",'r')
u_get=u_info.read()
u_info.close()
u_list=u_get.split()
print(u_list)
list.append(register_name,register_pwd)
f1=open('u_dict.txt','w')
if i in list:
    f1.write(i)
f1.close()
