from time import *

import time


def procedure():
    time.sleep(2.5)


def orginal_algorithm(a, b, c):
    ans = 1
    a = a % c
    for i in range(b):
        ans = (ans * a) % c
    return ans


def quick_algorithm(a, b, c):
    a = a % c
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans


t1 = time.clock()
a = eval(input("底数:"))
b = eval(input("指数:"))
c = eval(input("模:"))
print("朴素算法结果%d" % (orginal_algorithm(a, b, c)))
print("朴素算法耗时:%f" % (time.clock() - t1))
t2 = time.clock()
print("快速幂算法结果%d" % (quick_algorithm(a, b, c)))
print("快速幂算法耗时:%f" % (time.clock() - t2))
