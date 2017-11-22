#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
age_of_summer = 4
#guess_age=int(input("guess age: "))
for count in range(3):
    guess_age=int(input("guess age: "))
    if guess_age == age_of_summer:
        print("Good boy ,You got it.")
        break
    elif guess_age > age_of_summer:
        print("Think smaller...")
    else:
        print("Think bigger...")
#上面for 正常走完了才执行else，如果不正常走完就不执行else
else:
    print("You have tried too many times...")