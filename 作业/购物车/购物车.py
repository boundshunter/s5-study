#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
init() #系统初始化，读所有商品信息，保存到一个全局变量中
1、启动程序后，输入用户名，密码，如果第一次登录，让用户输入工资，然后打印商品列表
login() #认证登录
register() #新用户注册
show_product_list() #展示商品编号，名称，价格

2、允许用户根据商品编号购买商品
user_choice() #让用户输入选择的商品编号或者 q ，如果q就调用show_this_time_shopping_log并
3、用户选择商品后，检测余额是否够用，够就直接扣款，不够就提醒
balance_enough() #检查余额
add_cart() #放入购物车，并高亮显示，扣费，并调用日志信息
4、可随时退出，退出时，打印已购买商品和余额
show_shopping_log() 显示用户购物日志
5、在用户使用过程中，关键输出，如余额，商品已加入购物车等消息，需高亮显示

6、用户下一次登陆后，输入用户名，密码，直接回到上次的状态，即上次消费的余额什么的，还是那些，再次登录可继续购买
save_user_status() #用户信息存回文件
7、允许查询之前消费记录
shopping_log() #添加到本次消费日志和用户信息日志中

show_this_time_shop_log()
show_user_balance #显示余额并高亮显示