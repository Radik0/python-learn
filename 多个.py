import re

word_num = {}
with open('D:\\Debug\\python\\6.txt', 'rb') as f1:
    message = ''
    for line in f1:
        message += str(line.rstrip())

word_num['爱国'] = len(str(re.findall('爱国', message)))
word_num['祖国'] = len(str(re.findall('祖国', message)))
word_num['孙中山'] = len(str((re.findall('孙中山', message))))
print(word_num)
coding = "gbk"
import re

word_num = {}
with open('D:\\Debug\\python\\1.txt') as f1:
    message = ''
    for line in f1:
        message += str(line)
words = re.split(':|\n', message)
for word in words:
    word_num[word] = len(re.findall(word, message))
print(word_num)
