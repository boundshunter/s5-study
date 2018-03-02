#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import json
from core import db_handler
from conf import settings

def dump_account(account_data):

    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path,account_data['user'])

    with open(account_file,'w') as f:
        json.dump(account_data,f)

    return True


def load_account(account_id):

    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path,account_id)

    with open(account_file,'r') as f:
        acc_data = json.load(f)
        return acc_data
