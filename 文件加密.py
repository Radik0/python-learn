#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 10:34
# @Author  : Huang
# @FileName: 文件加密.py
# @Software: PyCharm
import hashlib

shal = hashlib.sha1()
shal.update("Huang".encode("utf-8"))
osv = shal.hexdigest()
print(osv)

bx = bytes(osv, encoding="utf-8")
with open("1.txt", "wb")as f:
    f.write(bx)
