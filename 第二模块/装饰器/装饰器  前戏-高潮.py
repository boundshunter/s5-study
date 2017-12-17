
'''
def foo():
    print("In the foo")
    def bar():
        print("In the bar")

    bar()

foo()
'''

import time

# def deco():
#     print('in the func')
def timer(func):  # timeer(test1)   func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs) #  run test1()
        stop_time=time.time()
        print('the func run time is %s' % (stop_time-start_time))
    return deco  # 返回test1 内存地址

@timer  # test1=timer(test1)   @timer 相当于运行 timer(test1),test1传给func
def test1():
    time.sleep(3)
    print('in the test1')
@timer  # test2=timer(test2) = deco   test2() = deco()   test(name) = deco()
def test2(name,age):
    time.sleep(4)
    print('%s in the test2 age is '% (name,age))

# test1=deco(test1)
# test2=deco(test2)
# print(timer(test1))  # 打印test1内存地址
#把内存地址赋给test1
# test1=timer(test1)  # 这个赋值过程可以用 @timer来代替
#test1()  # 执行timer(test1)结果，在执行deco()，deco中 func（） = test（）上下还执行时间
test1()
test2('jfsu',11)




