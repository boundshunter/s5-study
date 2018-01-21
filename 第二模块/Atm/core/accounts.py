#
import json
from core import db_handler
from conf import settings

def dump_account(account_data):
    '''

    :param account_data:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" % (db_path, account_data['id'])

    with open(account_file,'w') as f:
        json.dump(account_data,f)
    return True

