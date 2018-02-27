#
import json
from core import db_handler
from conf import settings

def dump_account(account_data):
    '''
    数据 dump 入指定路径文件，文件名为账户ID
    :param account_data:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account_data['id'])

    with open(account_file,'w') as f:
        json.dump(account_data,f)
    return True


def load_balance(account_id):
    '''
    显示余额
    :param account_id:
    :return:  acc_data = account_data
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account_id)

    with open(account_file,'r') as f:
        acc_data = json.load(f)
        return acc_data


