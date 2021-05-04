#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 9:18
# @Author  : Huang
# @FileName: 冒泡排序.py
# @Software: PyCharm
array = [1, 2, 5, 3, 6, 8, 4]
for i in range(len(array) - 1, 0, -1):
    print(i)
    for j in range(0, 1):
        print(j)
        if array[j] > array[i]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
