'''
装饰器 基础知识
    1、函数即变量
    2、不能修改被装饰函数的源代码
    3、不能修改被装饰函数的调用方式


装饰器实现
1、函数即变量
2、高阶函数
    a:把一个函数名当做实参传递给另一个函数(不修改呗装饰函数情况下，添加功能）
    b:返回值中包含函数名 （不修改被装饰函数的调用方式)
3、嵌套函数


嵌套函数：
# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#     bar() #局部变量调用才能输出内部结果
# foo()  # 运行结果 只有 in the foo 因为  bar是局部变量函数，在内部调用才可以输出

# 高阶函数 +  嵌套函数 -》 装饰器


# 全局作用于和局部作用域
x = 0
def grandpa():
    #x=1
    print(x)   # x = 0
    def dad():
        x=2
        print(x)  #  不定义 x = 0 定义 x = 定义值
        def son():
            #x=3
            print(x) # x 取值 由内而外 一层层去找作用域
        son()
    dad()
grandpa()

门牌号  内容
函数即变量
test()
x=1    test 相当于 x

匿名函数 没有函数名，lamda 会被内存直接回收掉。

函数即变量
定义一个函数相当于把函数体给了 函数名

'''
#高阶函数
import  time
# def test(func):
#     #print(func)  #调用把 func = bar    test(bar)调用
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print('run time is %s'%(stop_time-start_time))
# def bar():
#     time.sleep(3)
#     print('in the bar')
# test(bar)  #相当于 func = bar   func(） = bar()
#调用方式变化了，之前调用方式 bar()
#下面解决 不修改调用方式

def test(func):
    print(func)
    return func

@test
def bar():
    time.sleep(3)
    print('in the bar')



# t= test(bar)
# #print(t)
# t()  # t = bar

# bar = test(bar)  #  等于 @test

bar()  # 不改变调用方式


