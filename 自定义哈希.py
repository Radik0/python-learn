#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 14:51
# @Author  : Huang
# @FileName: 自定义哈希.py
# @Software: PyCharm
def my_hash(x):
    return (x % 7) ^ 2


x = int(input("请输入数字"))
print(my_hash(x))
print(my_hash(1))
print(my_hash(2))

import hashlib

md5 = hashlib.md5()
data = 'hello,word'
md5.update(data.encode('utf-8'))
print(md5.hexdigest())

print(hash(1))
print(hash(1.0))
print(hash('abc'))
print(hash('abcdefg'))
