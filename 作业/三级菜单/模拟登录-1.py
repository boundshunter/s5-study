# __Author__: sujunfeng
# 1、用户输入账号密码进行登录
# 2、用户信息保存在文本内
# 3、用户密码输入错误三次后锁定用户

user_info_data = {
    "jfsu":'abc123!',
    "xixi":"123,4!a",
    "hanhan":"!a!b!c"
}
import sys
import os

# 字典写入文件
with open("userinfo.txt",'w+') as f:
    f.write(str(user_info_data))

# 从文件中读出字典
with open("userinfo.txt",'r') as f:
    info=f.read()
    user_info=eval(info)

# 提示输入用户
username = input("请输入您的用户名 -->:")


# 初始化
count = 0
exit_flag = False

# 循环开始
while not exit_flag:
    if username in user_info:
        password = input("请输入您的密码-->:")
        pwd = user_info.get(username)

        while True:
            if pwd == password:
                print("欢迎回来，亲爱的 %s" % username)
                sys.exit()
            else:
                print("对不起，您的密码错误，你还有 %s 次输入机会" % (3-count))
                password = input("请重新输入密码-->:")
                if count <= 1:
                    if pwd == password:
                        print("欢迎回来，亲爱的 %s" % username)
                        sys.exit()
                    else:
                        count += 1
                        #print(count)
                        continue
                else:
                    print("您的用户已锁定，请联系管理员解锁")
                    sys.exit()
    else:
        print("您的用户名输入错误,退出程序")
        exit_flag = True


