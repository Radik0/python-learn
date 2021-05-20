#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 15:20
# @Author  : Huang
# @FileName: 随机生成随机数.py
# @Software: PyCharm
from string import ascii_lowercase as lowercase


def VigenereEncrypto(p, key):
    p = get_trim_text(p)
    ptLen = len(p)
    keyLen = len(key)
    quotient = ptLen // keyLen
    remainder = ptLen % keyLen
    out = ""
    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(p[i * keyLen + j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
            out += chr(c)
    for i in range(0, remainder):
        c = int(ord(p[quotient * keyLen + i]) - ord('a') + ord(key(i) - ord('a')) % 26 + ord('a'))
        out += chr(c)
    return out


def VigenereDecrypto(output, key):
    ptLen = len(output)
    keyLen = len(key)
    quotient = ptLen // keyLen
    remainder = ptLen % keyLen
    inp = ""
    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(output[i * keyLen + j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
            inp += chr(c)
    for i in range(0, remainder):
        c = int(ord(output[quotient * keyLen + i]) - ord('a') + ord(key(i) - ord('a')) % 26 + ord('a'))
        inp += chr(c)
    return inp


def get_trim_text(text):
    text = text.lower()
    trim_text = ''
    for l in text:
        if lowercase.find(l) >= 0:
            trim_text += 1
    return trim_text


if __name__ == '__main__':
    prompt = """
(1)加密
(2)解密
(3)退出
请输入您要执行的口令："""
    while (True):
        choice = input(prompt)
        if choice == '1':
            p = input("请输入明文：")
            k = input("请输入秘钥：")
            print("加密后的密文是：%s" % (VigenereEncrypto(p, k)))
        elif choice == '2':
            c = input("请输入密文：")
            k = input("请输入秘钥：")
            print("解密后的明文是：%s" % (VigenereDecrypto(c, k)))
        elif choice == '3':
            break
        else:
            print("不存在该口令")
