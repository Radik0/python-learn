# # encoding: utf-8
# """
# @description: morse编码与解码
# @author: huang
# @time: 2020-06-04 22:02
# @file: morseCode.py
# @version: python3.8.1
# """
#

a2mo_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
             'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
             'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
             'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
             'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
             '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
             }
mo2a_dict = dict(zip(a2mo_dict.values(), a2mo_dict.keys()))


def hgl30_start():
    """
    程序入口
    :return: NULL
    """
    choose = input("编码请按1，解码请按 0:")
    if choose == "0":
        try:
            hgl_jiema()
        except:
            print("请输入格式正确的摩尔斯电码")

    if choose == "1":
        try:
            hgl_bianma()
        except:
            print("只能输入字母数字")

    else:
        print('erroy.')


def hgl_jiema():
    """
    摩尔斯电码转换为字符串
    :return: NULL
    """
    crypto_text = input("请输入摩尔斯电码: ")
    morse_key = crypto_text.strip().split(" ")
    plain_text = [mo2a_dict[key] for key in morse_key]
    plain_text = "".join(plain_text)
    print("摩尔斯解码后的明文为：", plain_text)


def hgl_bianma():
    """
    字符串编码成摩尔斯电码
    :return: NULL
    """
    crypto_text = ""
    plain_text = input("请输入要加密的明文：").strip().replace(" ", "")
    for word in plain_text:
        crypto_text += a2mo_dict[word] + " "
    print("编码后的摩尔斯电码为：", crypto_text)


hgl30_start()
