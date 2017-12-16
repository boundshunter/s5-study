# 不同的 站点用不同的登录方式
import time
user,passwd = 'jfsu','abc'
def  auth(func):
    def warpper(*args,**kwargs):
        username=input("username>>:")
        password=input("password>>:")

        if user == username and passwd == password:
            print("\033[31;1mWelcome back home %s\033[0m"% user)
            func(*args,**kwargs)

        else:
            print("\033[32;1mInvalid username or passwd\033[0m")
    return warpper()

def index():
    print("index")

@auth
def bbs():
    print("bbs")

@auth
def home():
    print("bbs")