#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
import shutil
# f1 = open("笔记1",encoding="utf-8")
# f2 = open("笔记2","w",encoding="utf-8")
#
# shutil.copyfileobj(f1,f2)


#简单方法
#shutil.copyfile("笔记2","笔记3")

# shutil.copytree("shutil模块","shutil模块tmp")

#shutil.rmtree("shutil模块tmp")

# 压缩文件
# shutil.make_archive("shutil_archive_test","zip","C:\Users\sjf\PycharmProjects\s4\zn.dongao.com 统计")
import zipfile
#单独压缩文件  zipfile
z = zipfile.ZipFile('zip_test.zip','w')
z.write('笔记1')
print("------")
z.write('笔记2')
z.close()


