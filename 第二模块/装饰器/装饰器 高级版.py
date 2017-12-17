# 实现不同页面使用不同登录方式
import time
user,passwd='jfsu','abc'

def auth(auth_type):
    print('the func is %s'% auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print('the wrapper is:',*args,**kwargs)
            if auth_type == 'local':
                username = input('Username:').strip() #去掉输入两边的空格
                password = input('Password:').strip()
                if user == username and  passwd == password:
                    print('\033[31;1mPass\033[0m')
                    res =  func(*args,**kwargs)  # from home
                    return res
                else:
                    exit('\033[42;1m Invild username or password\033[0m')
            elif auth_type == 'ldap':
                print("auth is ldap")

        return wrapper
    return outer_wrapper
# @auth
# def index():
#     print('welcome to my web \033[42;1m Index \033[0m')

@auth(auth_type="local")
def bbs():
    print('welcome to my \033[31;1mBBS\033[0m')

@auth(auth_type="ldap")   # home = wrapper()
def home():
    print('Welcome to my \033[35;1mHomepage\033[0m')
    return 'from home'

# index()
bbs()
home()