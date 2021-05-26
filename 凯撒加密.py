#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 20:59
# @Author  : Huang
# @FileName: 凯撒加密.py
# @Software: PyCharm
# Caesar Cipher

MAX_KEY_SIZE = 26


def hgl30_getMode():
    while True:
        # print('请选择加密或解密模式,或者选择暴力破解：')
        print('加密:encrypt(e):')
        print('解密:decrypt(d):')
        # print('暴力破解:brute(b)')
        mode = input().lower()  # 对输入的字符转换
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('请输入"encrypt"或"e"或"decrypt"或"d"或"brute"或"b"!')


def hgl10_getMessage():
    print('请输入你的信息：')
    return input()


def hgl100_getKey():
    key = 0
    while True:
        print('请输入密钥数字(1-%s)' % (MAX_KEY_SIZE))  # 定义凯撒加密的秘钥
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def hgl102getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


mode = hgl30_getMode()
message = hgl10_getMessage()
if mode[0] != 'b':
    key = hgl100_getKey()

print('你要翻译的信息是:')
if mode[0] != 'b':
    print(hgl102getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, hgl102getTranslatedMessage('decrypt', message, key))
