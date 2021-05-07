#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 9:40
# @Author  : Huang
# @FileName: 哈希算法.py
# @Software: PyCharm
def hashmap(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if hashmap.get(target - nums) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i


num
