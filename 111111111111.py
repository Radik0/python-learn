#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 11:07
# @Author  : Huang
# @FileName: 111111111111.py.py
# @Software: PyCharm

a = 1
b = 2
a, b = b, a
b, a = a, b
print(a, b)
