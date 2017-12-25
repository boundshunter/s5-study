#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
# print(root.tag)

# 遍历 xml 文件
#
# for child in root:
#     # print(child)
#     print(child.tag,child.attrib)
#     for i in child:
#         print(i.tag,i.text)

# 只遍历 year 节点

for x in root.iter("year"): #iter 方法去取 year
    print(x.tag,x.text)

# tag 和 text
# 标签和内容

# 修改 xml 文件

