#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 11:25
# @Author  : Huang
# @FileName: md5_加密_登入.py
# @Software: PyCharm
import hashlib

USER_LIST = []


def get_md5(data):
    obj = hashlib.md5("12:;idrsicwersdfsaersdfresdy54436jgfdsjdxff123ad".encode("utf-8"))
    obj.update(data.encode("utf-8"))
    result = obj.hexdigest()
    return result


def register():
    print("******用户注册******")
    while True:
        user = input("请输入用户名")
        if user == "N":
            return
        pwd = input('请输入密码')
        temp = {'username': user, 'password': get_md5(pwd)}
        USER_LIST.append(temp)


def login():
    print("********用户登入*******")
    user = input("请输入用户名:")
    pwd = input("请输入密码:")
    for item in USER_LIST:
        if item["username"] == user and item["passwd"] == get_md5(pwd):
            return True


register()
result = login()
if result:
    print("成功")
else:
    print("失败")
