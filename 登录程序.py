#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 14:22
# @Author  : Huang
# @FileName: 登录程序.py
# @Software: PyCharm
# login = {
#     'a': '123',
#     'b': '1231',
#     'c': '3213'
#
# }
# user = input('请输入用户名')
# psd = input('请输入密码')
# if psd == login.get(user):
#     print("登入成功")
# elif not (user in login):
#     print('用户不存在')
# elif user in login and not (psd in login):
#     print('密码错误')
# else:
#     print("全部错误")
# from Crypto.Cipher import DES
#
# key = b'abcdefgh'  # 密钥 8位或16位,必须为bytes
#
#
# def pad(text):
#     """加密函数，如果text不是8的倍数【加密文本text必须为8的倍数！】，那就补足为8的倍数
#     """
#     while len(text) % 8 != 0:
#         text += ' '
#     return text
#
#
# des = DES.new(key, DES.MODE_ECB)  # 创建一个DES实例
# text = 'Python rocks!'
# padded_text = pad(text)
# encrypted_text = des.encrypt(padded_text.encode('utf-8'))  # 加密
# print(encrypted_text)
# # rstrip(' ')返回从字符串末尾删除所有字符串的字符串(默认空白字符)的副本
# plain_text = des.decrypt(encrypted_text).decode().rstrip(' ')  # 解密
# print(plain_text)
# 示例：ECB模式, 比CBC少一个key, 其他用法等同
from Crypto.Cipher import DES
# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex
#
# key = 'abcdefgh'   # 秘钥,此处需要将字符串转为字节
# def pad(text):   # 加密内容需要长达16位字符，所以进行空格拼接
#     while len(text) % 16 != 0:
#         text += ' '
#     return text
#
# aes = AES.new(key.encode(), AES.MODE_ECB)  # 进行加密算法，模式ECB模式
#
# text = 'hello'   # 加密内容,此处需要将字符串转为字节
#
# encrypted_text = aes.encrypt(pad(text).encode())  # 进行内容拼接16位字符后传入加密类中，结果为字节类型
# encrypted_text_hex = b2a_hex(encrypted_text)
# print(encrypted_text_hex)
# #用aes对象进行解密，将字节类型转为str类型，错误编码忽略不计
# de = str(aes.decrypt(a2b_hex(encrypted_text_hex)), encoding='utf-8',errors="ignore")
# print(de[:len(text)])   # 获取str从0开始到文本内容的字符串长度。
# DES加密示例：

# from Crypto.Cipher import DES
# key = b'abcdefgh' # 密钥 8位或16位,必须为bytes
#
# def pad(text):
#     """加密函数，如果text不是8的倍数【加密文本text必须为8的倍数！】，那就补足为8的倍数
#     """
#     while len(text) % 8 != 0:
#         text += ' '
#     return text
#
# des = DES.new(key, DES.MODE_ECB) # 创建一个DES实例
# text = 'Python rocks!'
# padded_text = pad(text)
# encrypted_text = des.encrypt(padded_text.encode('utf-8')) # 加密
# print(encrypted_text)
# #rstrip(' ')返回从字符串末尾删除所有字符串的字符串(默认空白字符)的副本
# plain_text = des.decrypt(encrypted_text).decode().rstrip(' ') # 解密
# print(plain_text)
# 安装的PyCryptodome是一个低级密码基元的独立Python包。
from Crypto.Cipher import AES
from Crypto import Random

key = b'1234567887654321'  # 密钥
iv = Random.new().read(AES.block_size)  # iv是初始向量，在加密之前与明文做异或运算

# AES.block_size = len（'12345678'）=8
# Random.new() 返回一个类文件对象，该对象以密码方式输出随机字节,可以作为iv
print(iv)

# 加密
cipher = AES.new(key, AES.MODE_CFB, iv=iv)  # 使用AES加密算法中CFB模式
data = '中国'.enconde()  # python的编码函数
msg = cipher.encrypt(data)  # encrypt是一个加密工具包
print(msg)

# 解密
cipher2 = AES.new(key, AES.MODE_CFB, iv=iv)
msg2 = cipher2.decrypt(msg)  # decrypt解密工具包
print(msg)

print(data)

print(msg2.decode())  # python解码，将unicode解码为utf-8
