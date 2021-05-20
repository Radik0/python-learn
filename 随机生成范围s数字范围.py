#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 15:03
# @Author  : Huang
# @FileName: 随机生成数字范围.py
# @Software: PyCharm
import random

a = int(input())
b = int(input())
c = int(input())
print(random.randrange(a, b, c))
