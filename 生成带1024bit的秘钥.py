#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 14:36
# @Author  : Huang
# @FileName: 生成带1024bit的秘钥.py
# @Software: PyCharm
from Crypto import Random
from Crypto.PublicKey import RSA

random_gen = Random.new().read
rsa = RSA.generate(1024, random_gen)
private_pem = rsa.exportKey()
with open('private_pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('public_pem', 'wb') as f:
    f.write(public_pem)
