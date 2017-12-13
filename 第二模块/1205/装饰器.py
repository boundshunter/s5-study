import time
# 高阶函数  +  嵌套函数 = 》 装饰器


def timer(func):  # 嵌套函数
    def decorator(*args,**kwargs):  # 高阶函数  之前 func 是传递给 decorator的
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))
    return decorator


@timer  # 相当于 相当于重新赋值  test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')


@timer
def test2(name, age):
    print('test2:', name, age)


#  高阶函数
# def decorator(func):
#     start_time = time.time()
#     # func
#     func()
#     stop_time = time.time()
#     print('run time is %s' % (stop_time-start_time))
#     return func


# print(decorator(test2))  # 此处 func=test2 func获得test2内存中地址 func() 相当于  test2()

#test2 = decorator(test2)  # python 内置了 一种方法 让谁可以嵌套，就在谁上面添加 @timer 相当于

#test2()

#  函数嵌套


test1()
test2('alex',33)

