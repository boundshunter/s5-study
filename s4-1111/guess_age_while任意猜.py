#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
age_of_summer = 4
#guess_age=int(input("guess age: "))
count=0
while count < 3:
    guess_age=int(input("guess age: "))
    if guess_age == age_of_summer:
        print("Good boy ,You got it.")
        break
    elif guess_age > age_of_summer:
        print("Think smaller...")
    else:
        print("Think bigger...")
    count+=1
    if count == 3:
        continue_confirm=input("Do you want to keep tring..."
                               "if you want keep tring press any button,or ctrl+c to cancel.")
        if continue_confirm != 'n':
            count=0
