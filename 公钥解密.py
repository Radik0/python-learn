#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 15:24
# @Author  : Huang
# @FileName: 公钥解密.py
# @Software: PyCharm
import base64

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Sig_pk

name = 'musen'
data = "d8O8EKGGUNn63tF1GxRJwgcCiW3ezU0NR0zUsEt+7sAXwSGf9OgngJWM75WCprRJxmcSLpXI/r8goIkO7z9uCrz+c4XDovIp8bNON26rS3JIC2uOoaQ90hkCDwxE+UjxN1n4mzfEK3RI82YMaoEJ1SUPCztfXFvE3NznPM9FwKw="
data = base64.b64decode(data)
key = open("public_pem").read()
rsakey = RSA.importKey(key)
sha_name = SHA.new(name.encode())
signer = Sig_pk.new(rsakey)
result = signer.verify(sha_name, data)
print(result)
