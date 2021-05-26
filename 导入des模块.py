#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 10:33
# @Author  : Huang
# @FileName: 导入des模块.py
# @Software: PyCharm
__author__ = 'hgl'

from Crypto.Cipher import DES

key = b'abcdefgh'


def pad(text):
    while len(text) % 8 != 0:
        text += ''

    return text


des = DES.new(key, DES.MODE_ECB)
text = 'i am chinese'
padded_text = pad(text)
print(padded_text)
encrypted_text = des.encrypt(padded_text.encode('utf-8'))
print(encrypted_text)

plaint_ext = des.decrypt(encrypted_text).decode().rstrip(" ")
print(plaint_ext)
