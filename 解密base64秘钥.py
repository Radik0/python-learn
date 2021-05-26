#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 14:43
# @Author  : Huang
# @FileName: 解密base64秘钥.py
# @Software: PyCharm
import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

msg = "bbAPvrWyJdSHj3pspw1D0ktrTGxJVCF+yZWR8cTeE0MWQnCMqStL9z9Mt/ARp25Hv+OFPlSC2UWiY2G8mKom/NxkwqkAGMwic1e4y9z/RFSDW5RCUOxRdqOAlneHgbsseRBg4GgWookLGgXx3zeUDEKQNRorHFQXOINxhpZJg2Ww="
msg = base64.b64decode(msg)
privatekey = open("private_pem").read()
rsakey = RSA.importKey(privatekey)
cipher = PKCS1_v1_5.new(rsakey)
text = cipher.decrypt(msg, "DecryptError")
print(text)
