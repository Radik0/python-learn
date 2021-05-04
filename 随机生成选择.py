#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 15:25
# @Author  : Huang
# @FileName: 随机生成选择.py
# @Software: PyCharm
import random

string = 'nice to meet you'
tup = {'nice', 'to', 'meet', 'you'}
lst = {'nice', 'to', 'meet', 'you'}
dic = {'a': 1, 'b': 2, 'c': 3}
print(random.sample(string, 2))
print(random.sample(tup, 2))
print(random.sample(lst, 2))
# ...
# ['m', 'i']
# ['you', 'nice']
# ['nice', 'to']
# ...
