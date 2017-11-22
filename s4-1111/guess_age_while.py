#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han
age_of_summer = 4
#guess_age=int(input("guess age: "))
count=0
while True:
    if count >= 3:
        break
    guess_age=int(input("guess age: "))

    if guess_age == age_of_summer:
        print("Good boy ,You got it.")
        break
    elif guess_age > age_of_summer:
        print("Think smaller...")
    else:
        print("Think bigger...")
    count+=1