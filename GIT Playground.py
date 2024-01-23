# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:01:43 2023

@author: revans

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

from git import Repo
repo = Repo('https://github.com/revans-ball/test.git')

name = input('Enter your name')
age = int(input('Enter your age'))

current_year = 2023
year_100 = (100-age) + current_year

print(name + ", the year that you will turn 100 years old is " + str(year_100))