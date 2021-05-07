#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 8:54
# @Author  : Huang
# @FileName: 散列函数.py
# @Software: PyCharm
def judee_e(r):
    n = 1
    while r >= (10 ** n):
        n = n + 1
    return 0


def midsquare(l):
    r = l * l
    n = judee_e(r)

    if n % 2 == 1:
        mid_n = (n // 2) + 1
        count_n = mid_n - 2
        while count_n != 0:
            r = r // 10
            count_n = count_n - 1
        r = r % 1000
        return r


x = [142, 124, 1245, 938, 172]
r = [0] * len(x)
for i in x:
    r[x.index(i)] = midsquare(i)
print(x)
x_square = [0] * len(x)
for i in x:
    x_square[x.index(i)] = i ** 2
print(x_square)
