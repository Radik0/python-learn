#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 14:12
# @Author  : Huang
# @FileName: 判断素数.py
# @Software: PyCharm

import random
import time


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
        # tem = pow(a, P-1)
        # tem2 = tem % P
        # 快速求幂取余
        tem2 = quickPowMod(a, P - 1, P)
        if tem2 != 1:
            flag = 1
            break

    if flag == 0:
        print("{0} is prime".format(P))
    elif flag == 1:
        print("{0} is not prime".format(P))
    else:
        print("error")


# 对素数进行判定，同时还能验证算法正确率
# prime,prime2中都是素数
def test1():
    prime = [9998581, 9999071, 9999163, 9999167, 9999217, 9999221, 9999397, 9999713, 9999929, 9999991]
    prime2 = [111111111111229, 111111111111233, 111111111111389, 111111111111443, 111111111111527, 519111111111683,
              719111111111683, 919111111111553, 919111111111679, 919111111111681]
    sumTime = 0
    maxTime = 0
    for P in prime2:
        start = time.time()
        Miler_Rabin(P)
        end = time.time()
        timeUse = end - start
        if maxTime < timeUse:
            maxTime = timeUse
        sumTime = sumTime + (timeUse)
    print("平均用时{0}s".format(sumTime / len(prime)))
    print("最坏用时{0}s".format(maxTime))


# 对随机数进行判断
def test2():
    sumTime = 0
    maxTime = 0
    for i in range(0, 100):
        P = random.randint(100000000000000000000000000000, 999999999999999999999999999999)
        start = time.time()
        Miler_Rabin(P)
        end = time.time()
        timeUse = end - start
        if maxTime < timeUse:
            maxTime = timeUse
        sumTime = sumTime + (timeUse)
    print("平均用时{0}s".format(sumTime / 100))
    print("最坏用时{0}s".format(maxTime))


if __name__ == '__main__':
    test1()
