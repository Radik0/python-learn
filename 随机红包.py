#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 9:45
# @Author  : Huang
# @FileName: 随机红包.py
# @Software: PyCharm
import random


def hgl12(money, amount):
    while amount:
        if amount == 1:
            yield float('%2f' % money)  # 您可能听说过，带有 yield 的函数在 Python 中被称之为 generator（生成器）
            # https://www.cnblogs.com/coder2012/p/4990834.html
        else:
            # uniform() 方法将随机生成下一个实数，它在 [x, y] 范围内
            money1 = random.uniform(0, money)
            money2 = random.uniform(1 / amount, 3 / amount) * money1  # 除以红包个数
            money -= float('%2f' % money2)  # 保留一位小数
            yield float('%2f' % money2)
        amount -= 1


x = int(input('请输入红包金额:'))
y = int(input("请输入你要发的红包个数:"))
g = hgl12(x, y)
print(list(g))
