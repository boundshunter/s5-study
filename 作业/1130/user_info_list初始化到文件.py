__author__ = 'sujunfeng'
user_info_dict = {
    'jfsu':{
        'password':'abc123!',
        'salary':30000,
        'buying_list':[]
    },
    'mmm':{
        'password':'123123',
        'salary':50000,
        'buying_list':[]
    }
}

with open('user_info_list.txt','w',encoding="utf-8") as f_init:
    f_init.write(str(user_info_dict))