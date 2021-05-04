# 交换两个数
# num1=int(input('请输入第一个数:'))
# num2=int(input('请输入第二个数:'))
# print('交换前的num1=%d,num2=%d' % (num1,num2))
# num1,num2=num2,num1
# print('交换后的num1=%d,num2=%d' % (num1,num2))

# 三个数比大小
# def maxmin(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             print('max is %d' % (num1))
#         else:
#             print('max is %d' % (num3))
#     else:
#         if num2>num3:
#             print('max is %d' % (num2))
#         else:
#             print('max is %d' % (num3))

# 公倍数
# num1=int(input('输入第一个数'))
# num2=int(input('输入第二个数'))
# num3=int(input("输入第三个数"))
# maxmin(num1,num2,num3)
# def gongyue(a, b):
#     while(b!=0):
#         temp = a % b
#         a=b
#         b=temp
#     return a
#
# def gongbei(a,b):
#     return a*b / gongyue(a, b)
#
#
# a=int(input())
# b=int(input())
#
#
# print(gongbei(a,b))
# print(gongyue(a,b))


# import numpy as np
# import  matplotlib.pyplot as plt
# x=np.random.randn(1000)
# y1=np.random.rand(len(x))
# y2=5+np.exp(x)
# ax1=plt.subplot(121)
# plt.scatter(x,y1,color='red',alpha=0.5,edgecolors='red',label='no coll')
# plt.xlabel('no coll')
# plt.xlim(-4,4,2)
# plt.ylim(-5,25,5)

# plt.grid(True)
# plt.legend(loc=1)
# ax2=plt.subplot(122,sharex=ax1,sharey=ax1)
# plt.scatter(x,y2,color="yellow",alpha=0.5,edgecolors='red',label='coll')
# plt.xlim(-4,4,2)
# plt.ylim(-5,25,5)
# plt.grid(True)
# plt.legend(loc=2)
# plt.show()


# x=np.random.randn(10000)
# y1=np.random.rand(len(x))
# y2=5+np.exp(x)
#
# ax1=plt.subplot(121)
# plt.scatter(x,y1,color='red',alpha=0.5,edgecolors='red',label='no corr')
# plt.xlim(-4,4,2)
# plt.ylim(-5,25,5)
# plt.xlabel('no corr')
# plt.grid(True)
# plt.legend(loc=1)
# ax2=plt.subplot(122,sharex=ax1,sharey=ax1)
# plt.scatter(x,y2,alpha=0.5,color='#FFF1FF',edgecolors='red',label='corr')
# plt.xlim(-4,4,2)
# plt.ylim(-5,25,5)
# plt.xlabel('corr')
# plt.grid(True)
# plt.legend(loc=2)
# plt.savefig('D:\\24\\1.png',dpi=500)
# plt.show()
#
