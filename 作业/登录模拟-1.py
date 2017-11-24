#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

#模拟登录
#用户输入账户，密码
#用户密码输入错误，三次后锁定

#没有的用户可以注册，加入字典,写入文件

user_dict = {
    "jfsu":"sjf319726",
    "xixi":"123456",
    "hanhan":"1234!@#",
    "sheyizi":"15210420306",
}
print(user_dict)
'''
f_write = open("u_dict.txt",'w')
for user_dic in user_dict:
    f_write.write(user_dic)
    f_write.write('\n')
f_write.close()

lock_list = ['xixi'] #初始化一个列表，列表可以从db中读取
name=input("登录用户--->:")
#print(user_dict.get(name)) #提取密码 ，name对应value
#user_dict[name] = "xxx" #修改用户
#user_dict.setdefault(name,value) # 添加字典
def login():
    if name not in lock_list: # 判断输入是否在 锁定列表
        done = False   #定义初始化值
        while not done:
            if name in user_dict.keys(): #判断用户名是否在字典中 ，如果在就执行下面
                pwd=input("登录密码--->:") #输入密码
                password=user_dict.get(name) #密码按照用户名对应取值
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
                            #print(lock_list) # 打印锁定列表
                        done=True #退出
            else: #用户不存在 ，准许注册，写入dict
                print("There is no user of %s，please register." % name)
                register_name = input("register_name:")
                register_pwd = input("register_pwd:")
                user_dict.setdefault(register_name,register_pwd)  #注册，写入dict
                #把最后字典写入文件

                #print("Your name is :",user_dict[register_name] ,"\n", "Your passwd is :", user_dict.get(register_name))

                done = True
        else:
            done = True
    else: #判断名字在锁定列表，提示用户联系管理员
        print("账户被锁定，请联系管理员 tel:18095272096")
        exit
if __name__ == '__main__': #固定写法，可以选择调用函数顺序
    login()
'''