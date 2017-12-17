#单线程下 并发    nginx  epoll

#生产者消费者模型
def consumer(name):
    print('%s 开吃包子'% name)
    while True:
        baozi = yield  # 中断状态记录，循环等待 发包子
        print('%s包子来了，被%s吃了' %(baozi,name))

# c=consumer('jfsu')
# c.__next__()
# b1="猪肉白菜"
# c.send(b1) # 相当于  给yield赋值后并且 执行 c.__next__()
#
# # c.send(b1) # 唤醒并且传递值
# # c.__next__ # 只唤醒
import time
def producer(name):
    c1 = consumer('xixi')
    c2 = consumer('hanhan')
    c1.__next__() #第一次调用， 返回print('%s 开吃包子'% name) 初始化准备好吃包子
    c2.__next__() # 第一次调用，返回  print('%s 开吃包子'% name)
    for i in range(5):  # 循环5次，每次吃2个包子
        time.sleep(1)
        print('\033[32;1m包子来了，%s吃包子\033[0m'%name)
        print(i)
        c1.send(i) #第二次调用传值
        c2.send(i)

producer('孩子们')
# 单线程下的并行效果，我们叫携程
