import random


def quieKPowMod(a, n, m):
    re = 1
    base = a % m
    while (n > 0):
        tem = n & 1
        if (tem):
            re = (re * base) % m
        base = (base * base) % m
        n >>= 1
    return re


def Miler_Rabin(p):
    m = 10
    flag = 0
    for i in range(0, m):
        a = random.randint(2, p - 1)
        tem2 = quieKPowMod(a, p - 1, p)
        if tem2 != 1:
            flag = 1
            break
    if flag == 0:
        print("{0} is prime".format(p))
    elif flag == 1:
        print("{0} is not prime".format(p))
    else:
        print("error")


if __name__ == '__main__':
    while (1):
        p = int(input("请输入一个数字:"))
        Miler_Rabin(p)
