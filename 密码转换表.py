# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# # @Time    : 2021/4/15 9:42
# # @Author  : Huang
# # @FileName: 密码转换表.py.py
# # @Software: PyCharm
# AlphaBet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
#             "V", "W", "X", "Y", "Z"]
# alphaBet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
#             "v", "w", "x", "y", "z"]
# AlphaBet1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
#              "v", "w", "x", "y", "z"]
# key = list(input("输入密钥："))
# miwen = input("输入密文：")
# keyf = []
# mingwen = ""
#
#
# def chuli_key():
#     x = 0
#     for i in key:
#         z = 0
#         x = 0
#         for a in key:
#             if i == a:
#                 x = x + 1
#                 if x == 2:
#                     key.pop(z)
#                     x = 0
#             z += 1
#     print(key)
#
#
# def add_key():
#     i = 0
#     while i < len(key):
#         AlphaBet1[i] = key[i]
#         i += 1
#     k = len(key)
#     j = 0
#     for i in AlphaBet:
#         if key.count(i) == 0:
#             AlphaBet1[k] = i
#             k += 1
#
#
# chuli_key()
# add_key()
# for i in miwen:
#     if i.isspace() == True:
#         mingwen = mingwen + ''
#         continue
#     else:
#         if ord(i) <= ord("Z"):
#             mingwen = mingwen + alphaBet[AlphaBet1.index(i)]
#         elif ord(i) >= ord("a"):
#             mingwen = mingwen + AlphaBet1[alphaBet.index(i)]
# print(key)
# print(alphaBet)
# print(AlphaBet)
# print(AlphaBet1)
# print(mingwen)
# input("按任意键退出")


# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 14:37
# @Author  : Huang
# @FileName: 包含数字,小写字母和大写字母的验证码.py
# @Software: PyCharm
# import random
#
#
# def get_code():
#     code_list = []
#     #   for i in range(10):   # 0~9
#     for i in range(48, 57):  # ASCII表示的数字0-9 chr()方法将10进制的数字传化为对应的字符
#         code_list.append(chr(i))  # 将迭代器追加到列表
#     for i in range(65, 91):  # A-Z
#         code_list.append(chr(i))
#     for i in range(97, 123):  # a-z
#         code_list.append(chr(i))
#     code = random.sample(code_list, 6)  # 用于截取列表的指定长度的随机数，返回的是列表
#     code_num = ''.join(code)  # 将列表里的元素以指定的字符连接生成一个新的字符串
#     return code_num
#
#
# print(get_code())
import random as r

la = [chr(i) for i in range(65, 91)]  # 定义随机大写字母A/Z
lb = [chr(i) for i in range(97, 123)]  # 定义随机小写字母a/z
# ld = [chr(i) for i in range(48, 58)]  # 定义随机数字0/9
sum = la + lb
a = input("请输入")
while a in sum:
    break
print(sum)
# print(ld)
# print(la)
# print(lb)
# labd = la + lb + ld  # 将大小写字母和随机数字相加
# r.shuffle(labd)  # 利用随机函数定义字符串
# r.shuffle(ld)  # 利用随机函数定义数字
# hgl = r.sample(labd, 3) + r.sample(ld, 1)
# # r.shuffle(lb)
# # hgl=r.sample(lb,4)
# # r.shuffle(hgl)
# code_num = ''.join(hgl)
# print(str(code_num))
