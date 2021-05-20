#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 14:22
# @Author  : Huang
# @FileName: 哈希lib.py
# @Software: PyCharm
#
# 1 加密哈希算法并判断类型
# import hashlib
# obj = hashlib.md5()
# obj.update('小马过河'.encode("utf-8"))
# result = obj.hexdigest()
# print(result)
# print(obj, type(obj))
# 2 普通哈希加密
# import hashlib
#
# a = hashlib.md5()
# a.update('小马过河'.encode("utf-8"))
# print(a)
# 3 哈希 使用个人信息优化加密
# import hashlib
#
# b = hashlib.md5("1587317249@qq.com".encode("utf-8"))
# b.update("12121".encode("utf-8"))
# c = b.hexdigest()
# print(c)

# 4 哈希 md5 定义函数 实现
# import hashlib
#
#
# def get_md5(data: object) -> object:
#     obj = hashlib.md5('1587317249@qq.com'.encode("utf-8"))
#     obj.update(data.encode("utf-8"))
#     result = obj.hexdigest()
#     return result
#
#
# val = get_md5('小马过河')
# print(val)
