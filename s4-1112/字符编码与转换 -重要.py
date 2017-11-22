#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
# 重要
'''
#日本编码想在中文运行
#先日文转unicode , unicode再转GBK
#python3默认所有字符都是unicode

#打印系统默认编码
import sys
print(sys.getdefaultencoding())

GBK 转 UTF-8编码的过程
1、首先解码为 unicode编码 decode
2、然后编码为utf-8编码  encode

UTF-8 转 GBK 编码过程
1、首先解码为unicode编码  decode
2、然后编码为 GBK编码   encode

# python 2.x 中脚本
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
print(sys.getdefaultencoding())

#默认使用asicii

#目前使用为 窗口utf-8 option里面配置的
s = "您好"

s_to_unicode = s.decode("utf-8") #utf-8 转 unicode   decode
print(s_to_unicode)
print("utf-8 ---> unicode")
s_to_gbk = s_to_unicode.encode("gbk") #unicode 转 gbk
print(s_to_gbk)
print("unicode ---> gbk")
#下面从 gbk 转回 utf-8

s_to_unicode2 = s_to_gbk.decode("gbk") #gbk 转 unicode
print(s_to_unicode2)
print("gbk ---> unicode")
s_to_utf8 = s_to_unicode2.encode("utf-8")#unicode 转  utf-8
print(s_to_utf8)
print("unicode ---> utf8")



#####最简单的转换方法
import os

name = "你非常好你好你好"

new_name = name.decode("utf-8").encode("GBK") #先通过 decode 把utf-8转换成unicode 在通过 encode把 Unicode 转换成 gbk
print(new_name)

name_new = new_name.decode("gbk").encode("utf-8") #再将gbk转换成 utf-8

                                                  #先把 gbk --decode--> unicode,再把 unicode ---encode--->utf-8
print(name_new)


####例：
s = u"你好"  #这种情况下 u的意思是将s转换为unicode

s_to_gbk = s.encode("gbk") # 这样将s转为gbk可以直接使用
print(s_to_gbk)

以上均为 python2.x环境使用方法
'''
import sys
s=u"你好"
print(sys.getdefaultencoding())
s_2312 = s.encode("gb2312")
print(s_2312)
gb2312_to_utf8 = s_2312.decode("gb2312").encode("utf-8")
print(gb2312_to_utf8)
utf8_to_gbk = gb2312_to_utf8.decode("utf-8").encode("gbk")
print(utf8_to_gbk)
# gb2312 和 gbk 编码是一样的，只是我们哈希的碰巧都有了，所以编码一样。