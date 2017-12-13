#-*- coding:utf-8 -*-
# Author:summer_han

'''
设置单元格样式
'''
import xlsxwriter
import time
# import
# wb = xlsxwriter.Workbook._add_sheet('左侧栏点击')

wb = xlsxwriter.Workbook('test.xls')
# 定义 4个 sheet
ws1 = wb.add_worksheet('左侧栏点击')
ws2 = wb.add_worksheet('经济法基础')
ws3 = wb.add_worksheet('初级会计实务')
ws4 = wb.add_worksheet('用户学习习惯')

sheet_left_header = ['初级会计职称','初级经济法','初级会计实务']

sheet_law_header = ['初级会计职称','经济法基础','自由学习','学习计划	','查看课程目录	','学习记录	','快速复习','统计','听课记录',
                 '课程收藏','课程笔记','做题记录','试题收藏','试题笔记','我的错题','自主演练','机考','答疑','下载','勘误']

sheet_primary_header = ['初级会计职称','初级会计实务','自由学习','学习计划','查看课程目录','学习记录','快速复习','统计','听课记录',
                        '课程收藏','课程笔记', '做题记录','试题收藏','试题笔记','我的错题','自主演练','机考','答疑','下载','勘误'	]

sheet_user_header = ['初级会计职称','初级会计职称','经济法基础-自由学习','经济法基础-计划学习',
                 '初级会计实务-自由学习','初级会计实务-计划学习']

sheet_user_1_header = ['智能推送','任务','考点','智能推送','任务','考点','智能推送','任务']
sheet_user_2_header = ['总','我会了','课','题','答疑']

#定义头部风格 12号蓝色字体 黑框，粗体，背景色，居中对齐，缩进
header_format = wb.add_format({
  'border': 1,                         # 边框
  'bold': 1,                           # 粗体
  'bg_color': '#C6EFCE',              # 背景色
  'valign': 'center',                 # 对齐方式 居中
  'indent': 1,                         # 缩进
  'font_color': 'blue',               # 字体颜色
  'font_size' : 12,                    # 字体大小
})

#定义body风格  左对齐，12号字体,加边框
body_format = wb.add_format({
  'valign':'left',
  'font_size':12,
  'border': 1,
})
x=1  # x = 1 第二行
y=0  # y = 0 第一列
# head_pv = 'pv'
# head_uv = 'uv'
headings = [ 'pv', 'uv']
data = [
    'date',
    ['pv','uv'],
    [2, 3, 4, 5, 6, 7],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
    ]

ws2.write(x,y, data[0])  # 第二行 第一列 ，时间头
ws2.write_row(x,y+1, data[1])  # 第二行第二列 取 pv,uv写入 行写
ws2.write_column(x+1,y,data[2])  # 第三行，第一列  2,3,4,5,6,7
ws2.write_column(x+1,y+1, data[3])  # 第三行 ， 第二列  pv 值 10,40....
ws2.write_column(x+1,y+2, data[4])  # 第三行 ， 第三列  uv 值 30,60...
#for i in range(2,4,2):
ws2.merge(0,0,1,2,123)

#ws2.merge((x-1),(x-1),(y+1),(y+2),sheet_law_header[0])

y=y+2
ws2.write_row(x,y+1, headings)
ws2.write_column(x+1,y+1, data[3])
ws2.write_column(x+1,y+2, data[4])

y+=2
ws2.write_row(x,y+1, headings)
ws2.write_column(x+1,y+1, data[3])
ws2.write_column(x+1,y+2, data[4])
wb.close()


