#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 9:20
# @Author  : Huang
# @FileName: 随机生成大小写.py
# @Software: PyCharm
import random


def get_code(n):
    code = ''
    for i in range(n):
        num = str(random.randint(0, 9))
        apl_upper = chr(random.randint(65, 90))
        apl_lower = chr(random.randint(97, 122))
        c = random.choice([num, apl_lower, apl_upper])
        code += c
        return code


n = int(input())
print(get_code(n))
