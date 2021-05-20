n = 3
nums = []
for i in range(n):
    num1 = int(input('请输入一个整数'))
    nums.append(num1)
print(nums)
for num in nums:
    max = 0
    min = 0

    if num < min:
        min = num
    elif num > max:
        max = num
print(max)
print(min)
