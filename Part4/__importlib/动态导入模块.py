#!/usr/bin/env python
#__Author__ : Summer
#-*- coding: utf-8 -*-
# 导入方法 __import__('import_lib.metaclass') # 解释器内部使用的方法
# 官方建议写法 importlib.import_module('import_lib.metaclass')

# __import__('lib.aa')

# import sys,os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
#
# from lib.aa import ccc

#写法1 mod = importlib.import_module('lib.aa')
import importlib
mod = importlib.import_module('lib.aa')
obj = mod.ccc()
print(obj.name)


# 写法2为python 内部解释方法
# 写法2 __import__("import_lib.metaclass")
mod = __import__('lib.aa')
print(mod.aa)

obj = mod.aa.ccc()
print(obj.name)

# 写法2.1 通过反射完成
# instance = getattr(mod.aa,"ccc")
# obj = instance() #相当于 from lib import aa  obj=aa.ccc
# print(obj.name)