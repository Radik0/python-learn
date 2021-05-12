#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 14:22
# @Author  : Huang
# @FileName: 哈希lib.py
# @Software: PyCharm
import hashlib

obj = hashlib.md5()
obj.update('小马过河'.encode("utf-8"))
print(obj, type(obj))
