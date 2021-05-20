#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 9:42
# @Author  : Huang
# @FileName: 密码转换表.py.py
# @Software: PyCharm
AlphaBet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
alphaBet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
AlphaBet1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
key = list(input("输入密钥："))
miwen = input("输入密文：")
keyf = []
mingwen = ""


def chuli_key():
    x = 0
    for i in key:
        z = 0
        x = 0
        for a in key:
            if i == a:
                x = x + 1
                if x == 2:
                    key.pop(z)
                    x = 0
            z += 1
    print(key)


def add_key():
    i = 0
    while i < len(key):
        AlphaBet1[i] = key[i]
        i += 1
    k = len(key)
    j = 0
    for i in AlphaBet:
        if key.count(i) == 0:
            AlphaBet1[k] = i
            k += 1


chuli_key()
add_key()
for i in miwen:
    if i.isspace() == True:
        mingwen = mingwen + ''
        continue
    else:
        if ord(i) <= ord("Z"):
            mingwen = mingwen + alphaBet[AlphaBet1.index(i)]
        elif ord(i) >= ord("a"):
            mingwen = mingwen + AlphaBet1[alphaBet.index(i)]
print(key)
print(alphaBet)
print(AlphaBet)
print(AlphaBet1)
print(mingwen)
input("按任意键退出")
