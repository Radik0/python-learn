#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 10:37
# @Author  : Huang
# @FileName: 密码登入测试.py
# @Software: PyCharm
user = ['xy1', 'sy2', "sy3"]
pwd = ['abc', 'abc123', '1234', "123123"]

pwd_user = {
    'syz': '123456',
    'sy1': '123'
}
user1 = input('请输入用户名')
pwd1 = input("请输入密码")

for i in range(0, 3):
    if user1 == user[i] and pwd1 == pwd[i]:
        print("登入成功")
        break
    elif not (user1 in user):
        print("用户不存在")
        break
    else:
        print("密码错误")
        break
