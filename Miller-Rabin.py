#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 20:15
# @Author  : Huang
# @FileName: 1.py
# @Software: PyCharm


import random


# 快速求幂取模
def hgl11(a, n, m):  # 定义函数引入变量
    re = 1
    base = a % m
    while (n > 0):
        tem = n & 1  # 对tem进行判断
        if (tem):
            re = (re * base) % m
        base = (base * base) % m
        n >>= 1
    return re


def hgl12(P):
    m = 10
    flag = 0
    for i in range(0, m):
        # 调用函数,随机从2和P-1中抽取数字赋值给a
        a = random.randint(2, P - 1)
        # 调用上面定义的函数
        tem2 = hgl11(a, P - 1, P)
        if tem2 != 1:
            flag = 1
            break
    # 对flag进行判断
    if flag == 0:
        print("{0} is prime".format(P))
    elif flag == 1:
        print("{0} is not prime".format(P))
    else:
        print("error")


if __name__ == '__main__':
    # https://www.zhihu.com/question/49136398
    while (1):
        P = int(input("请输入一个数字："))
        hgl12(P)
