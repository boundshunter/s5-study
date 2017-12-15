#-*- coding:utf-8 -*-
import xlsxwriter
import time

w_b = xlsxwriter.Workbook('Data.xls')

ws_1 = w_b.add_worksheet('左侧栏点击')
ws_2 = w_b.add_worksheet('经济法基础')
ws_3 = w_b.add_worksheet('初级会计实务')
ws_4 = w_b.add_worksheet('用户学习习惯')

sheet_left_title = ['初级会计职称','初级经济法','初级会计实务']

sheet_law_title = ['初级会计职称','经济法基础','自由学习','学习计划	','查看课程目录	','学习记录	','快速复习','统计','听课记录',
                 '课程收藏','课程笔记','做题记录','试题收藏','试题笔记','我的错题','自主演练','机考','答疑','下载','勘误']

sheet_primary_title = ['初级会计职称','初级会计实务','自由学习','学习计划','查看课程目录','学习记录','快速复习','统计','听课记录',
                        '课程收藏','课程笔记', '做题记录','试题收藏','试题笔记','我的错题','自主演练','机考','答疑','下载','勘误'	]

sheet_user_1_title = ['初级会计职称','初级会计职称','经济法基础-自由学习','经济法基础-计划学习',
                 '初级会计实务-自由学习','初级会计实务-计划学习']

sheet_user_2_title = ['智能推送','任务','考点','智能推送','任务','考点','智能推送','任务']
sheet_user_3_title = ['总','我会了','课','题','答疑']


#定义头部风格 12号蓝色字体 黑框，粗体，背景色，居中对齐，缩进
header_format = w_b.add_format(
        {
                'border': 1,                         # 边框
                'bold': 1,                           # 粗体
                'bg_color': '#C6EFCE',              # 背景色
                # 'align': {'vertical': 'middle',
                #          'horizontal': 'center'
                # },                 # 对齐方式 居中
                'align':'center',
                'valign':'vcenter',
                'indent': 1,                         # 缩进
                'font_color': 'blue',               # 字体颜色
                'font_size' : 12,                    # 字体大小
                # 'font':{'color':'blue',
                #         'size':12

                # },
        }
)

#定义body风格  左对齐，12号字体,加边框
body_format = w_b.add_format({
  'valign':'left',
  'font_size':12,
  'border': 1,
})


def merge_left():  # 定义头部信息函数
    ws_1.write_blank(0,0,'',header_format)
    ws_1.write_blank(1,0,'',body_format)
    x = 0  # 定义最上面一格
    y = 0
    for i in sheet_left_title:
        # print(i)
        ws_1.merge_range(x,y+1,x,y+2,i,header_format)
        y+=2
    return True
# merge_left() # 定义头部信息
def merge_law():  # 定义头部信息函数
    ws_2.write_blank(0,0,'',header_format)
    ws_2.write_blank(1,0,'',body_format)
    x = 0  # 定义最上面一格
    y = 0
    for i in sheet_law_title:
        # print(i)
        ws_2.merge_range(x,y+1,x,y+2,i,header_format)
        y+=2
    return True

def merge_primary():  # 定义头部信息函数
    ws_3.write_blank(0,0,'',header_format)  # 行首空格设置格式
    ws_3.write_blank(1,0,'',body_format)
    x = 0  # 定义最上面一格
    y = 0
    for i in sheet_primary_title:
        # print(i)
        ws_3.merge_range(x,y+1,x,y+2,i,header_format)
        y+=2
    return True

pu_title = ['pv','uv']

def pu_write():  # 写入pv,uv
    x=0
    y=0
    for n in range(1,6,2):
        ws_1.write_row(x+1,y+n,pu_title,body_format)
    for s in range(1,40,2):
        ws_2.write_row(x+1,y+s,pu_title,body_format)
        ws_3.write_row(x+1,y+s,pu_title,body_format)
    for u in range(1,58,2):
        ws_4.write_row(x+3,y+u,pu_title,body_format)


def merge_user():
    ws_4.write_blank(0,0,'',header_format)  # 行首空格设置格式
    for i in range(1,4):
        ws_4.write_blank(i,0,'',body_format)
    x=3
    y=1
    ws_4.merge_range(x-3,y,x-3,y+1,sheet_user_1_title[0],header_format)
    ws_4.merge_range(x-3,y+2,x-3,y+13,sheet_user_1_title[1],header_format)
    ws_4.merge_range(x-3,y+14,x-3,y+23,sheet_user_1_title[2],header_format)
    ws_4.merge_range(x-3,y+24,x-3,y+35,sheet_user_1_title[3],header_format)
    ws_4.merge_range(x-3,y+36,x-3,y+45,sheet_user_1_title[4],header_format)
    ws_4.merge_range(x-3,y+46,x-3,y+57,sheet_user_1_title[5],header_format)

    ws_4.merge_range(x-2,y+2,x-2,y+3,sheet_user_2_title[0],body_format)   #智能推送
    ws_4.merge_range(x-2,y+24,x-2,y+25,sheet_user_2_title[0],body_format)
    ws_4.merge_range(x-2,y+46,x-2,y+47,sheet_user_2_title[0],body_format)

    # ws_4.merge_range()
    # for item in range(1,60,20):
    #     print(item)


# def p_u_date():
pu_write()
merge_left()
merge_law()
merge_primary()
merge_user()
w_b.close()