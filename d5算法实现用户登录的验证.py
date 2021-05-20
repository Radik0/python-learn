#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 14:52
# @Author  : Huang
# @FileName: d5算法实现用户登录的验证.py
# @Software: PyCharm
import hashlib

db = {}


def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()


def calc_md5(password, username):
    return get_md5(password + username + 'the-Salt')


def register(username, password):
    db[username] = calc_md5(password, username)


def login(username, password):
    pw = db.get(username)
    if not pw:
        print('user is not exist')
    else:
        if calc_md5(password, username) == pw:
            print('user login success')
        else:
            print('wrong password')


register('user', 'rightpassword')
username = input("请输入用户名：")
password = input("请输入密码：")
login(username, password)
