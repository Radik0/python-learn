#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 14:10
# @Author  : Huang
# @FileName: 公钥加密基于base64.py
# @Software: PyCharm
# 先运行生成秘钥的文件

import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

msg = "zry"
key = open("public_pem").read()
public_key = RSA.importKey(key)
pk = PKCS1_v1_5.new(public_key)
encrypt_text = pk.encrypt(msg.encode())
result = base64.b64encode(encrypt_text)
print(result)
