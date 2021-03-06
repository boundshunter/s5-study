#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

本节作业: 选课系统

角色:学校、学员、课程、讲师 ( 不同角色视角不同，讲师，批作业，学生，上什么课，报道)
要求:
1. 创建北京、上海 2 所学校 # 至少2个分校  每个学校也是一个单独的实例，
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开 # 每一个课程都是一个单独的示例，课程周期大纲价格，详细信息
#课程和学校关联起来，组合方法，o1，o2，o3，实例关联，也就是组合，老师和学校之间的关联关系，把老师关联到学校里
# 一个学校多个老师怎么办？学校类里弄一个teacherlist,生成一个老师，加入teacherlist

3. 课程包含，周期，价格，通过学校创建课程
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级 # 生成一个学员，关联
5. 创建讲师角色时要关联学校，  # 讲师要么在北京，要么在上海
6. 提供两个角色接口 # 学员，讲师角度看到的信息
6.1 学员视图， 可以注册， 交学费， 选择班级， #
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
6.3 管理视图，创建讲师， 创建班级，创建课程  # 选做

7. 上面的操作产生的数据都通过pickle序列化保存到文件里 # json或者pickle 保存在文件

至少含有这几个类： 讲师类，学员类，课程类，学校类
