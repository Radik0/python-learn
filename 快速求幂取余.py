#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 14:15
# @Author  : Huang
# @FileName: 快速求幂取余.py
# @Software: PyCharm

import random


# 快速求幂取模
def quickPowMod(a, n, m):
    re = 1
    base = a % m
    while (n > 0):
        tem = n & 1
        if (tem):
            re = (re * base) % m
        base = (base * base) % m
        n >>= 1
    return re


def Miler_Rabin(P):
    # 循环次数m
    m = 10

    flag = 0
    for i in range(0, m):
        # a是2-P-1的随机数
        a = random.randint(2, P - 1)
        # 直接求幂取余
        tem = pow(a, P - 1)
        tem1 = tem % P
        # 快速求幂取余
        tem1 = quickPowMod(a, P - 1, P)
        if tem1 != 1:
            flag = 1
            break

    if flag == 0:
        print("{0} is prime".format(P))
    elif flag == 1:
        print("{0} is not prime".format(P))
    else:
        print("error")


if __name__ == '__main__':

    while (1):
        P = int(input("请输入一个数字："))
        Miler_Rabin(P)
