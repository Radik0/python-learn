#
# import re
# with open('5.txt','rb') as f1:
#     message=''
#     for line in f1:
#         message+=str(line.rstrip())
#
# counter=re.findall('1',message)
# print(len(message))


# import collections
#
#
# with open('6.txt','rb') as file1:#打开文本文件
#     str1=file1.read().split(' ')#将文章按照空格划分开
#
# print("原文本:\n %s"% str1)
# print ("\n各单词出现的次数：\n %s" % collections.Counter(str1))
# print(collections.Counter(str1)['祖国'])#以字典的形式存储，每个字符对应的键值就是在文本中出现的次数
