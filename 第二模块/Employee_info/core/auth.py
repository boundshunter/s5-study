#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import os
import json
from core import db_handler
from conf import settings


def check_user(phone):
    '''
    使用手机号对用户唯一性 验证，如果手机号存在则报错。
    :param phone:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    db_file = "%s/%s.json" %(db_path,phone)

    if os.path.isfile(db_file):
        with open(db_file) as f:
            user_info = json.load(f)
            return user_info
    else:
        return None