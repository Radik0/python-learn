#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 15:03
# @Author  : Huang
# @FileName: 快速求幂.py
# @Software: PyCharm
def kuaishu(a, n, m):
    re = 1
    base = a % m
    while (n > 0):
        tem = n & 1
        if (tem):
            re = (re * base) % m
        base = (base * base) % m
        n >>= 1
        return re


a, n, m = input()
kuaishu(a, n, m)
