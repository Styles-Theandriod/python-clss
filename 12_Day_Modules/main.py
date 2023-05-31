
# from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
# print(fullname('Asabneh','Yetayeh')) 
# print(total(1, 9))
# mass = 100;
# weight = mass * g
# print(weight)
# print(p)
# print(p['firstname'])

# import os

# os.mkdir('people-of-God')
# os.chdir('people-of-God')
# print(os.getcwd())
# os.rmdir()

# import sys
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))


# from statistics import *

# Roct_Of_ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
# print(mean('men:',Roct_Of_ages))
# print(median(Roct_Of_ages)) 

# print(stdev(Roct_Of_ages))

# print('\n')
# print('\n')
# print('\n')
# from math import pi
# print(pi)

# import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# print('\n')
# print('\n')
# print('\n')

# from random import random, randint
# print(random())

# print(randint(5, 20))

# def myInput():
#     nme = input('enter your nme ')
#     print(nme)
# myInput()


# from datetime import datetime

# now = datetime.now()
# day = now.day                   # 8
# month = now.month               # 7
# year = now.year                 # 2021
# hour = now.hour                 # 7
# minute = now.minute             # 38
# second = now.second
# timestamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)


# now = datetime.now()
# t = now.strftime("%H:%M:%S")

# print("time", t)


# from datetime import date

# today = date(year=2023, month=5, day=30)
# new_year = date(year=2024, month=1, day=1)
# time_left_for_newyear = new_year - today

# print('time_left_for_newyear', time_left_for_newyear)

# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst))


# numbers = range(2, 7)
# print(list(numbers))

# args = [2, 7]
# numbers = range(*args)
# print(numbers)

# def packing_person_info(**kwargs):
#     for key in kwargs:
#         print("{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name="Asabeneh",
#       country="Finland", city="Helsinki", age=250))


# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]

# lst = [0, *lst_one, *lst_two]


import re

txt = 'I love to teach python and javaScript'
match = re.match('I LOVE to teach', txt, re.I)


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('first',txt,re.I)
span = match.span()


# start, end = span

# substring = txt[start:end]
# print(substring)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

language = re.findall('language', txt, re.I)

matches = re.findall('Python|python|pYthon', txt)
print(matches)

language = re.sub('Python|python', "javascript", txt, re.I)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))


f = open('ex.txt')
txt = f.read()
f.close()
print(txt)
    