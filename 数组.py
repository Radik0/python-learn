#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 8:38
# @Author  : Huang
# @FileName: 数组.py
# @Software: PyCharm
array = [1, 2, 5, 3, 6, 8, 4]

print(array)
a = array[0::]
# 从第0位开始往后计算
print('a:的是', a)
b = array[:-1:]
# print (array[6])
# print(array[-1])
# 从第0位到第负一位,也就是第六位
print('b:的是', b)
c = array[3:-3:]
# 从第三位到第-3位
print('c:的是', c)
d = array[::2]
# 间隔为2
print('d:的是', d)
e = array[::3]
print('e:的是', e)
f = array[::4]
print('f:的是', f)
g = array[::-1]
print('g:的是', g)
# 间隔为-1,倒叙
