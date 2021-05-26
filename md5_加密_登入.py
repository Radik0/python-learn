#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 11:25
# @Author  : Huang
# @FileName: md5_加密_登入.py
# @Software: PyCharm
import hashlib

USER_LIST = []


def hgl01_get_md5(data):
    obj = hashlib.md5("12:;idrsicwersdfsaersdfresdy54436jgfdsjdxff123ad".encode("utf-8"))  # 引入md5 加密随机数
    obj.update(data.encode("utf-8"))  # 定义uft8格式u
    result = obj.hexdigest()  # 调用哈希算法
    return result


def hgl_02register():
    print("******用户注册******")
    while True:
        user = input("请输入用户名")
        if user == "N":
            return
        pwd = input('请输入密码')
        temp = {'username': user, 'pwd': hgl01_get_md5(pwd)}  # 将读入的字符加入到字符之中
        USER_LIST.append(temp)


def hgl_03login():
    print("********用户登入*******")  # 用户登入检测
    user = input("请输入用户名:")
    pwd = input("请输入密码:")
    for item in USER_LIST:
        if item["username"] == user and item["pwd"] == hgl01_get_md5(pwd):  # 与字典之中的数据对比
            return True


hgl_02register()
result = hgl_03login()
if result:
    print("成功")
else:
    print("失败")
