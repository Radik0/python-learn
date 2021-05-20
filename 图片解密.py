#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:38
# @Author  : Huang
# @FileName: 图片解密.py
# @Software: PyCharm
# 安装的PyCryptodome是一个低级密码基元的独立Python包。
# from Crypto import Random
# from Crypto.Cipher import AES
#
# key = b'1234567887654321'  # 密钥
# iv = Random.new().read(AES.block_size)  # iv是初始向量，在加密之前与明文做异或运算
#
# # AES.block_size = len（'12345678'）=8
# # Random.new() 返回一个类文件对象，该对象以密码方式输出随机字节,可以作为iv
# print(iv)
#
# # 加密
# cipher = AES.new(key, AES.MODE_CFB, iv=iv)  # 使用AES加密算法中CFB模式
# data = '中国'.encode()  # python的编码函数
# msg = cipher.encrypt(data)  # encrypt是一个加密工具包
# print(msg)
#
# # 解密
# cipher2 = AES.new(key, AES.MODE_CFB, iv=iv)
# msg2 = cipher2.decrypt(msg)  # decrypt解密工具包
# print(msg)
#
# print(data)
#
# print(msg2.decode())  # python解码，将unicode解码为utf-8


# 安装的PyCryptodome是一个低级密码基元的独立Python包。
from Crypto.Cipher import AES
from Crypto import Random

key = b'1234567887654321'  # 密钥
iv = Random.new().read(AES.block_size)  # iv是初始向量，在加密之前与明文做异或运算

# AES.block_size = len（'12345678'）=8
# Random.new() 返回一个类文件对象，该对象以密码方式输出随机字节,可以作为iv
print("iv为:" + str(iv))

# 加密
cipher = AES.new(key, AES.MODE_CFB, iv)  # 使用AES加密算法中CFB模式
data = '中国'.encode()  # python的编码函数
print(data)  # utf-8转换成unicode编码形式
msg = cipher.encrypt(data)  # encrypt是一个加密工具包
print("传递的密文：" + str(msg))

# 解密
cipher2 = AES.new(key, AES.MODE_CFB, iv)
msg2 = cipher2.decrypt(msg)  # decrypt解密工具包
print("解密密文：" + str(msg))

print(data)
print(msg2.decode())  # python解码，将unicode解码为utf-8
