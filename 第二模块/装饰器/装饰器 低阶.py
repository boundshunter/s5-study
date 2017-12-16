
# 统计函数运行时间
import time
def timer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("The run time is %s"%(stop_time-start_time))
    return warpper()
@timer  # 相当于 相当于重新赋值  test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')


@timer
def test2(name, age):
    time.sleep(4)
    print('test2:', name, age)
