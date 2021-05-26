#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 14:51
# @Author  : Huang
# @FileName: 私钥签名.py
# @Software: PyCharm
import base64

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Sig_pk

name = "musen"

key = open("private_pem", "r").read()
rsakey = RSA.importKey(key)
data = SHA.new(name.encode())
sig_pk = Sig_pk.new(rsakey)
sign = sig_pk.sign(data)
result = base64.b64encode(sign)
data = result.decode()
print(data)
