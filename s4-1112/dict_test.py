#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
"""info = {
    "stu01":"jfsu",
    "stu02":"xix",
    "stu03":"hanhan"
}
print(info.keys())
print(info.values())

for key in info:
    #print(key)
    print(key,info[key])
print(info.items())

for key,value in info.items(): #字典转换列表
    print(key,value)


info_b = {
    'stu04':"lili",
    'stu01':'jfsu',
    123:456
}
info.update(info_b) #去重合并
print(info)



#c = dict.fromkeys([5,6,7],"test")
c = dict.fromkeys([6,7,8],[1,{"user":"susan"},{"age":"13"}]) #dict.fromkeys 初始化一个字典
#print(c)
#print(c.items())
#for k,v in c.items():
#    print(k,v[1]) 打印 key对应values 列表中第二个元素
#c.pop(6)   #删除 key:6 和对应的value
print(c.get(6,5)) #打印字典key:6 对应值，如果有就打印，没有返回None


c = {
    "欧美":{
        "www.youporn.com":["免费多","质量一般"],
        "www.pornhub.com":["也很大","质量比YP好"],
        "letmedothistoyou.com":["多是自拍,高清","更新慢"],
        "x-art.com":["质量高","全部收费"]
    },
    "日韩":{
        "tokyo-hot":["不清真","收费"]
    },
    "港台":{
        "1024":["for free",'好人一生平安']
    }
}
#for k,v in c.items():
#    print(k,v)
#print(c.items())
#print(c.values())

c.setdefault("非洲",{"4096":[3,4]})
c.setdefault("非洲",{"4096":["免费","高清无码"]})
c["非洲"][0]=2048
print(c["非洲"])
"""

#字典
#创建
dict1 = {
    'key':'value',
    'key1':'value1'
}
a = [('key1','value1'),('key2','value2')]
dict1 = dict(a)
dict1 = {}.fromkeys(['key1','key2'],'default_value') #从键值创建dict
dict1 = dict(key1='value1',key2='value2')

#增加
dict1['key3']='value3' #字典可以自动添加
dict1.setdefault('key5','N/A') #如果不存在，就设置默认值

#删除
del dict1['key3']
print dict1.pop('key2')  #popitem随机删除 和列表的pop一样
#dict1.clear()  #深删除,即使有拷贝 也会被删除

#修改
if 'key1' in dict1:
    dict1['key1']='new_value_1'
#查找
if 'key1' in dict1:
    print dict1['key1']
if dict1.has_key('key1'):
    print dict1['key1']
print dict1.get('key3','not exists') #宽松访问
print dict1.keys(),dict1.values()

#拼接
dict2 = dict(key4 = 'value4') #从字典更新另一个字典
dict1.update(dict2)

