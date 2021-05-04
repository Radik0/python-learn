#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 15:09
# @Author  : Huang
# @FileName: 更快速的求幂.py
# @Software: PyCharm
from time import *


def orginal_algoithm(a, b, c):
    ans = 1
    a = a % c
    for i in range(b):
        ans = (ans * a) % c
    return ans


def quy(a, b, c):
    a = a % c
    ans = 1

    while b != 0:
        if b & 1:
            ans = (ans * a) % c
            b >>= 1
            a = (a * a) % c
    return ans


time = clock()
a = eval(input('底数'))
b = eval(input('指数'))
c = eval(input('摸'))
print('算法结果:%d' % (orginal_algoithm(a, b, c)))
print('算法耗时:%f' % (clock() - time))
time = clock()
print('算法结果:%d' % (quy(a, b, c)))
print('算法耗时:%f' % (clock() - time))
