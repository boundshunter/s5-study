#-*- coding:utf-8 -*-
# Author:summer_han

'''
设置单元格样式
'''
import xlsxwriter
import time
# wb = xlsxwriter.Workbook._add_sheet('左侧栏点击')
wb = xlsxwriter.Workbook('test.xls')
# 定义 4个 sheet
ws1 = wb.add_worksheet('左侧栏点击')
ws2 = wb.add_worksheet('经济法基础')
ws3 = wb.add_worksheet('初级会计实务')
ws4 = wb.add_worksheet('用户学习习惯')

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
# 定义默认 风格
# ws1.conditional_format()

head1 = '初级会计职称'
head2 = '初级经济法'
head3 = '初级会计实务'
head4 = '计划学习'
head5 = '查看课程目录'
head6 = '学习记录'
head7 = '快速复习'
head8 = '统计'
head9 = '听课记录'
head10 = '课程收藏'
head11 = '课程笔记'
head12 = '做题记录'
head13 = '试题收藏'
head14 = '试题笔记'
head15 = '我的错题'
head16 = '自主演练'
head17 = '机考'
head18 = '答疑'
head19 = '下载'
head20 = '勘误'
head21 = '初级会计职称-经济法基础'
head22 = '初级会计职称-初级会计实务'
head23 = '经济法基础-自由学习'
head24 = '经济法基础-计划学习'
head25 = '初级会计实务-自由学习'
head26 = '初级会计实务-计划学习'
head27 = '智能推送'
head28 = '任务学习'
head29 = '考点学习'
head30 = '我会了'
head31 = '课'
head32 = '题'
head33 = '答疑'
head_pv = 'pv'
head_uv = 'uv'

#l =[['','',''],]
#ws1.write_row('A5',l,body_format)

ws1.merge_range('B1:C1', head1, header_format)
ws1.merge_range('D1:E1',head2,header_format)
ws1.merge_range('F1:G1',head3,header_format)
ws1.write('B2',head_pv,body_format)
ws1.write('C2',head_uv,body_format)
ws1.write('D2',head_pv,body_format)
ws1.write('E2',head_uv,body_format)
ws1.write('F2',head_pv,body_format)
ws1.write('G2',head_uv,body_format)
# ws1.write_formula('B11','{=SUM(B3:B34)}')  # 定义总和
# for i in 'B2,D2,F2,H2,J2,L2,N2,P2,R2,T2,V2,X2,Z2,AB2,AD2,AF2,AH2,AJ2,AL2'.split(','):
#   ws2.write(i,head_pv,header_format)
date_time = time.strftime('%Y/%m/%d')
ws1.write('A3',date_time,body_format)

ws2.write
wb.close()


