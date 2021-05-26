#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 14:52
# @Author  : Huang
# @FileName: md5算法实现用户登录的验证.py
# @Software: PyCharm
import hashlib

db = {
    "username": "huang"
}


def hgl_01get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()


def hgl_02calc_md5(password, username):
    return hgl_01get_md5(password + username + 'the-Salt')


def hgl_03register(username, password):
    db[username] = hgl_02calc_md5(password, username)


def login(username, password):
    pw = db.get(username)
    if not pw:
        print('user is not exist')
    else:
        if hgl_02calc_md5(password, username) == pw:
            print('user login success')
        else:
            print('wrong password')


hgl_03register('user', 'rightpassword')
username = input("请输入用户名：")
password = input("请输入密码：")
login(username, password)
