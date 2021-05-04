x = int(input("请输入数字一:"))
y = int(input("请输入数字二:"))


def gy(m, n):
    r = int(m % n)
    while r != 0:
        m = n
        n = r
        r = int(m % n)
    print("{}和{}最大公约数为:{}".format(x, y, n))


gy(x, y)
