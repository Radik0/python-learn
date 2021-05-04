s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
f1 = open("D:\\Debug\\python\\1.txt", 'r+')
message = f1.read()
sum = 0
for i in message:
    if ('A' <= i <= 'Z'):
        sum = sum + 1
        for j in range(0, 26):
            if (s[j] == i):
                b[j] = b[j] + 1
print(sum)
print(b)
result = []
for i in range(0, 26):
    result.append((b[i] / sum))
    print(s[i], ":", (b[i] / sum) * 100)
