n = 3
nums = []
for i in range(10):
    num1 = int(input('请输入一个整数'))
    nums.append(num1)
print(nums)
for num in nums:
    max = 0
    min = 0
    if num > max:
        max = num
    elif min > num:
        min = num
print(max)
print(min)
