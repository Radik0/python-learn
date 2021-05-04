#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 14:59
# @Author  : Huang
# @FileName: 随机加密.py
# @Software: PyCharm
import math
import random


def prime_array():
    arrays = []
    for i in range(2, 100):
        x = prime(i, 2)
        if x:
            arrays.append(i)
    return arrays


def prime(n, text_divison):
    if math.sqrt(n) < text_divison:
        return True
    if n % text_divison == 0:
        return False
    else:
        return prime(n, text_divison + 1)


def co_prime(s):
    while True:
        e = random.choice(range(100))
        x = gcd(e, s)
        if x == 1:
            break
    return e


def gcd(a, b):
    if b == 0:
        return 0
    else:
        return gcd(a, a % b)


def find_d(e, s):
    for d in range(100000000):
        x = (e * d) % s
        if x == 1:
            return d


def main():
    a = prime_array()
    print('前一百个素数:', a)
    p = random.choice(a)
    q = random.choice(a)
    print('随机生成素数q p p=', p, 'q=', q)
    n = p * q
    s = (p - 1) * (q - 1)
    e = co_prime(s)
    print("根据互为质素的得出:e=", e)
    d = find_d(e, s)
    print('根据互为质素得出d=', d)
    print('gongyao: n=', n, 'e=', e)
    print('siyao: n=', n, 'd=', d)
    pbvk = (n, e, d)
    return pbvk


def generart_pbk_pvk(a, zx):
    pbk = (a[0], a[1])
    pvk = (a[0], a[2])
    if zx == 0:
        return pbk
    if zx == 1:
        return pvk


def encrrption(nw, ned):
    B = pow(nw, ned[1]) % ned[0]
    return B


def decode(nw, ned):
    C = pow(nw, ned[1]) % ned[0]
    return C


if __name__ == '__main__':
    pbvk = main()
    pbk = generart_pbk_pvk(pbvk, 0)
    A = int(input('输入铭文:'))
    print('加密中')
    B = encrrption(A, pbk)
    print('生成的密文是', B)
    pvk = generart_pbk_pvk(pbvk, 1)
    print('解密')
    C = decode(B, pvk)
    print('解密之后的是:', C)
    if A == C:
        print('成功')
