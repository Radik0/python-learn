#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 8:55
# @Author  : Huang
# @FileName: 随机生成四位验证码.py
# @Software: PyCharm
import random


def get_code(n):
    code = ''
    for i in range(n):
        num = random.randint(0, 9)
        code += str(num)
    return code


print(get_code(4))
