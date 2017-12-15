#-*- coding:utf-8 -*-
import xlsxwriter
import time







# #定义头部风格 12号蓝色字体 黑框，粗体，背景色，居中对齐，缩进
# header_format = w_b.add_format(
#         {
#                 'border': 1,                         # 边框
#                 'bold': 1,                           # 粗体
#                 'bg_color': '#C6EFCE',              # 背景色
#                 # 'align': {'vertical': 'middle',
#                 #          'horizontal': 'center'
#                 # },                 # 对齐方式 居中
#                 'align':'center',
#                 'valign':'vcenter',
#                 'indent': 1,                         # 缩进
#                 'font_color': 'blue',               # 字体颜色
#                 'font_size' : 12,                    # 字体大小
#                 # 'font':{'color':'blue',
#                 #         'size':12
#
#                 # },
#         }
# )
#
# #定义body风格  左对齐，12号字体,加边框
# body_format = w_b.add_format({
#   'valign':'left',
#   'font_size':12,
#   'border': 1,
# })


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

def get_title():
    pass
    d_title = {}
    d_title['左侧栏点击'] = {}
    d_title['经济法基础'] = {}
    d_title['初级会计实务'] = {}
    d_title['用户学习习惯'] = {}

    l_t = ['初级会计职称','初级经济法','初级会计实务']
    for i in l_t:
        d_title['左侧栏点击']['0_0_'+str(l_t.index(i))] = i.strip()

    l_t = ['初级会计职称','经济法基础','学习计划','查看课程目录','学习记录','快速复习','统计','听课记录','课程收藏','课程笔记','做题记录','试题收藏','试题笔记','我的错题','自主演练','机考','答疑','下载','勘误']
    for i in l_t:
        d_title['经济法基础']['0_0_'+str(l_t.index(i))] = i.strip()

    l_t = ['初级会计职称','初级会计实务','学习计划','查看课程目录','学习记录','快速复习','统计','听课记录', '课程收藏','课程笔记', '做题记录','试题收藏','试题笔记','我的错题','自主演练','机考','答疑','下载','勘误'	]
    for i in l_t:
        d_title['初级会计实务']['0_0_'+str(l_t.index(i))] = i.strip()

    l_t = ['初级会计职称','初级会计职称-经济法基础','初级会计职称-初级会计实务','经济法基础-自由学习','经济法基础-计划学习','初级会计实务-自由学习','初级会计实务-计划学习']
    for i in l_t:
        d_title['用户学习习惯'][str(l_t.index(i.strip()))] = i.strip()
    d_title['用户学习习惯']['0_0'] = ' '
    d_title['用户学习习惯']['0_0_0'] = ' '

    d_title['用户学习习惯']['1_0'] ='智能推送'
    d_title['用户学习习惯']['1_0_0'] = ' '

    d_title['用户学习习惯']['1_1'] = '任务'
    d_title['用户学习习惯']['1_1_0'] = '我会了'
    d_title['用户学习习惯']['1_1_1'] = '课'
    d_title['用户学习习惯']['1_1_2'] = '题'
    d_title['用户学习习惯']['1_1_3'] = '答疑'

    d_title['用户学习习惯']['2_0'] = '智能推送'
    d_title['用户学习习惯']['2_0_0'] = ' '

    d_title['用户学习习惯']['2_1'] = '任务'
    d_title['用户学习习惯']['2_1_0'] = '我会了'
    d_title['用户学习习惯']['2_1_1'] = '课'
    d_title['用户学习习惯']['2_1_2'] = '题'
    d_title['用户学习习惯']['2_1_3'] = '答疑'

    d_title['用户学习习惯']['3_0'] = '考点'
    d_title['用户学习习惯']['3_0_0'] = '我会了 '
    d_title['用户学习习惯']['3_0_1'] = '课'
    d_title['用户学习习惯']['3_0_2'] = '题'
    d_title['用户学习习惯']['3_0_3'] = '答疑'

    d_title['用户学习习惯']['4_0'] = '智能推送'
    d_title['用户学习习惯']['4_0_0'] = ' '
    d_title['用户学习习惯']['4_1'] = '任务'
    d_title['用户学习习惯']['4_1_0'] = '我会了'
    d_title['用户学习习惯']['4_1_1'] = '课'
    d_title['用户学习习惯']['4_1_2'] = '题'
    d_title['用户学习习惯']['4_1_3'] = '答疑'

    d_title['用户学习习惯']['5_0'] = '考点'
    d_title['用户学习习惯']['5_0_0'] = '我会了 '
    d_title['用户学习习惯']['5_0_1'] = '课'
    d_title['用户学习习惯']['5_0_2'] = '题'
    d_title['用户学习习惯']['5_0_3'] = '答疑'

    d_title['用户学习习惯']['6_0'] = '智能推送'
    d_title['用户学习习惯']['6_0_0'] = ' '
    d_title['用户学习习惯']['6_1'] = '任务'
    d_title['用户学习习惯']['6_1_0'] = '我会了'
    d_title['用户学习习惯']['6_1_1'] = '课'
    d_title['用户学习习惯']['6_1_2'] = '题'
    d_title['用户学习习惯']['6_1_3'] = '答疑'

    return d_title

def get_title_xy(sheetname,d_title,init_x=10,init_y=1):
    pass
    x=init_x
    y=init_y
    l_l = [7,2,40]

    d_t = d_title.get(sheetname,{})
    # print(len(d_t))
    d_t_be = {}
    l_base = []
    for l0 in range(l_l[0]):
        l = []
        by0 = y
        for l1 in range(l_l[1]):
            by1 =y
            for l2 in range(l_l[2]):
                l.append(str(l0))
                l.append(str(l1))
                l.append(str(l2))
                tk = '_'.join(l)
                tn = d_t.get(tk)
                if tn:
                    ey = y+1
                    # print(tn,'x=',x,' by=',y,'ey=',ey)
                    d_t_be[tk] = [x,y,ey]
                    l_base.append(tk)
                    y += 2
                l = []
            tk = str(l0)+'_'+str(l1)
            tn = d_t.get(tk)
            if tn:
                # print(tn,'x=',x,' by=',by1,'ey=',ey)
                d_t_be[tk] = [x-1,by1,ey]


        tk = str(l0)
        tn = d_t.get(tk)
        if tn:
            # print(tn,'x=',x,' by=',by0,'ey=',ey)
            d_t_be[tk] = [x-2,by0,ey]
    return d_t_be,l_base

def get_data(sheet,l_base):
    l_date = []
    d_data_old = {}
    d_data = {}

    l_date=['2017-01-01','2017-01-02','2017-01-03']
    for bi in l_base:
        l_pv = []
        l_uv = []
        for di in l_date:
            k_pv = str(di).strip()+'_'+str(bi).strip()+'_pv'
            k_uv = str(di).strip()+'_'+str(bi).strip()+'_uv'
            l_pv.append(d_data.get(k_pv,0))
            l_uv.append(d_data.get(k_uv,0))
        l_pv.append(sum(l_pv))
        l_uv.append(sum(l_uv))
        d_data[bi] = [l_pv,l_uv]
    # print(d_data)
    return l_date,d_data




def write_data(w_b,ws,d_xy,d_title_name,d_data=[],l_date=[]):
    l_pu = ['pv','uv']
    l_by = []
    l_x = []
    l_ey = []
    body_format = w_b.add_format({
  'valign':'left',
  'font_size':12,
  'border': 1,
})
    for tw in d_xy:
        x = d_xy[tw][0]
        by = d_xy[tw][1]
        ey = d_xy[tw][2]
        l_x.append(int(x))
        l_by.append(int(by))
        l_ey.append(int(ey))
        ws.merge_range(x,by,x,ey,d_title_name.get(tw,'--'),body_format)
        if len(tw.split('_')) == 3:
            ws.write_row(x+1,by,l_pu,body_format)
            ws.write_column(x+2,by,d_data.get(tw,[[],[]])[0],body_format)
            ws.write_column(x+2,by+1,d_data.get(tw,[[],[]])[1],body_format)

    ws.merge_range(min(l_x),min(l_by)-1,max(l_x)+1,min(l_by)-1,'Date',body_format)
    ws.write_column(max(l_x)+2,min(l_by)-1,l_date+['Totle:'],body_format)


def deal_sheet(w_b,sheet):
    pass

    ws = w_b.add_worksheet(sheet)
    x=10
    y=0
    d_xy,l_base = get_title_xy(sheet,d_title,x,y+1)
    # print(sheet)
    # print(d_xy)
    l_date,d_data = get_data(sheet,l_base)
    write_data(w_b,ws,d_xy,d_title.get(sheet,{}),d_data,l_date)

def main(l_sheet):
    pass
    w_b = xlsxwriter.Workbook('Data.xls')
    for sheet in l_sheet:
        deal_sheet(w_b,sheet)
    w_b.close()

if __name__=='__main__':
    l_sheet=['左侧栏点击','经济法基础','初级会计实务','用户学习习惯']
    d_title = get_title()
    # print(d_title)
    for i in d_title:
        print(i,d_title[i])
    main(l_sheet)
