
#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

# import re
# >>> a=re.match("inet","inet addr:10.0.1.110  Bcast:10.0.255.255  Mask:255.255.0.0")
# >>> a
# <_sre.SRE_Match object; span=(0, 4), match='inet'>
# >>> a=re.match("\w+","inet addr:10.0.1.110  Bcast:10.0.255.255  Mask:255.255.0.0")
# >>> a
# <_sre.SRE_Match object; span=(0, 4), match='inet'>
#
# 没匹配上返回none  匹配上了返回值
# import re
# # rel=re.findall('([\d\.]+|/|-|\+|\*)',exps)
# aaa="https://mv.dongaocloud.com/2b52/2bc2/1a5/fe3/3822170c83053b21716544a11e9a59b1/video.m3u8|122.246.3.109"
# # rel=re.findall('\|',aaa)
# # print(rel)
# print(aaa.split("|")[0],aaa.split("|")[1])
import  re

L1_Info = '''
---------电子产品列表-----------
1、samsung S9  -----  6999.0
2、xiao mi 2s  -----  2599.0
3、huawei p20  -----  5999.0

'''
# L1_Info_Dic = {
#     '1':['samsung S9','6999.0'],
#     '2':['xiao mi 2s','2599.0'],
#     '3':['huawei p20','5999.0']
# }

L1_Info_Dic = {
    'sam':'1111',
    'sbm':'2222',
    'scm':'3333'
}
for k,v in L1_Info_Dic.items():
    print('商品：'+k+'  ----  '+'价格:'+v)
