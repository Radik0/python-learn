def change(c, i):
    num = ord(c)
    if (num >= 33 and num <= 126):
        num = 33 + (num + i - 33) % (94)
    return chr(num)


def kaisa_jiami(string, i):
    string_new = ''
    for s in string:
        string_new += change(s, i)
    print(string_new)
    return string_new


def kaisa_jiemi(string):
    for i in range(0, 94):
        print('第' + str(i + 1) + '几种可能', end='')
        kaisa_jiami(string, i)


def main():
    print('请输入操作,')
    chioce = input('1为凯撒加密,2为凯撒穷举加密,请输入1,2')
    if chioce == '1':
        string = input('请输入需要加密的字符串')
        num = int(input('请输入秘钥key'))
        kaisa_jiami(string, num)
    elif chioce == '2':
        string = input('请输入需要加密的字符串')
        kaisa_jiemi(string)
    else:
        print('false')
        main()


if __name__ == '__main__':
    main()
