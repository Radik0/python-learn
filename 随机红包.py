#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 9:45
# @Author  : Huang
# @FileName: 随机红包.py
# @Software: PyCharm
import random


def bouns(money, amount):
    while amount:
        if amount == 1:
            yield float('%2f' % money)
        else:
            money1 = random.uniform(0, money)
            money2 = random.uniform(1 / amount, 3 / amount) * money1
            money -= float('%2f' % money2)
            yield float('%2f' % money2)
        amount -= 1

        x = int(input())
        y = int(input())
        g = bouns(x, n)
        print(list(g))
