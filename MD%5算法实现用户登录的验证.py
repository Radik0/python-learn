#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 22:34
# @Author  : Huang
# @FileName: MD%5算法实现用户登录的验证.py
# @Software: PyCharm
import hashlib

md5 = hashlib.md5()
sha1 = hashlib.sha1()
name = []
password = []
user = {}
dict(user)


def hgl01_get_md5(data):
    obj = hashlib.md5("12:;idrsicwersdfsaersdfresdy54436jgfdsjdxff123ad".encode("utf-8"))  # md5 加密
    # 引入md5 加密随机数
    obj.update(data.encode("utf-8"))  # 定义uft8格式u
    result = obj.hexdigest()  # 调用哈希算法
    return result


def hgl_032findLen(str):  # 验证字符长度
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


# 验证
la = [chr(i) for i in range(65, 91)]  # 定义随机大写字母A/Z
lb = [chr(i) for i in range(97, 123)]  # 定义随机小写字母a/z
yz = la + lb
ty = True
# 用户注册
while ty:

    choice = input('1：用户注册\t2：验证登录\tps:其他数字退出(切勿输入字母以外的东西)\n输入长度小于1')  # 对用户的输入进行判断
    if choice in yz or hgl_032findLen(choice) > 2:

        print("长度错误,输入错误")
        ty = False  # while 退出的条件
    else:
        choice = int(choice)

    while choice == 1:
        print('----用户注册----'.center(40))
        name_ = input('(用户名由数字、字母、符号组成)\n请输入要注册的用户名：')
        name.append(name_)  # 添加到name里
        password_ = input('(密码由数字、字母、符号组成)\n请设置用户密码')
        print(password_)  # 添加到password 里
        print('通过md5加密中...'.center(40))
        hgl01_get_md5(password_)  # 对输入的密码加密
        print(md5.hexdigest())
        password.append(md5.hexdigest())
        # 将用户名和密码保存到字典
        choice1 = input('注册成功！\b\n输入1返回\t输入2继续注册\t不能输入其他字符且长度小于1')
        if choice1 in yz or hgl_032findLen(choice1) > 2:

            print("长度错误")
            ty = False
            break
        else:
            choice1 = int(choice1)
            if choice1 == 1:
                break
            else:
                continue
    user = dict(zip(name, password))
    print(user)

    # 验证登录
    while choice == 2:
        print('----用户登入----'.center(40))
        _name = input('用户名:')
        if _name in user.keys():
            _password = input('密码：')
            print(_password)
            print('md5加密中...'.center(40))
            hgl01_get_md5(_password)
            print(md5.hexdigest())
            if md5.hexdigest() == user[_name]:
                print('登录成功！\n欢迎使用！'.center(40))
                break
            else:
                print('密码错误！'.center(40))
                continue
        else:
            print('用户名不存在！'.center(40))
            continue
