# import numpy as np
# import  matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['Simhei']      #中文显示
# plt.rcParams['axes.unicode_minus']=False        #负号显示
# plt.xlim(xmax=9,xmin=0)
# plt.ylim(ymax=9,ymin=0)
# plt.xlabel('X轴')
# plt.ylabel('Y轴')
# #5-8行的代码画了两条（0-9）的坐标轴并且分别设置两个坐标轴的标签为X轴、Y轴
# x1=np.random.normal(2,1.2,300)      #随机产生300个平均值为2，方差为1.2的浮点数。
# y1=np.random.normal(2,1.2,300)      #随机产生300个平均值为2，方差为1.2的浮点数。
# x2=np.random.normal(7,1.2,300)      #随机产生300个平均值为7，方差为1.2的浮点数。
# y2=np.random.normal(7,1.2,300)      #随机产生300个平均值为7，方差为1.2的浮点数。
# color1='#00CED1'        #男生的随机数，点的颜色
# color2='#DC143C'        #女生的随机数，点的颜色
# area=6**2       #点的面积，男女同款
# plt.scatter(x1,y1,s=area,c=color1,alpha=0.5,label='男生')
# plt.scatter(x2,y2,s=area,c=color2,alpha=0.5,label='女生')
# plt.plot([0,10],[10,0],linewidth='1',color='#696969')
# plt.legend()
# plt.title('类别统计图')
# plt.savefig(r'D:\\hgl\\黄国龙.png',dpi=300)
# plt.show()

# import numpy as np
# import  matplotlib.pyplot as plt
# x=np.random.randn(10000)
# y1=np.random.rand(len(x))
# y2=5+np.exp(x)
# ax1 = plt.subplot(121)
# plt.scatter(x,y1,color='red',alpha=0.5,edgecolors='#125365',label='no correl')
# plt.xlabel('no correlation')
# plt.xlim(-4,4,2)
# plt.ylim(-5,25,5)
# plt.legend(loc=1)
# plt.grid(True)
# ax2 = plt.subplot(122 ,  sharex=ax1,sharey=ax1 )
# plt.scatter(x,y2,color='blue',alpha=0.2,edgecolors='yellow',label='correl')
# plt.xlabel('strong correlation')
# plt.xlim(-4,4,2)
# plt.ylim(-5,25,5)
# plt.title('no corr')
# plt.legend(loc=2)
# plt.grid(True)
# plt.legend()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['Simhei']      #中文显示
# plt.rcParams['axes.unicode_minus']=False        #负号显示
# x = np.random.randn(1000)# 返回一组正态分布数据（1000组）
# y1 = np .random.rand(len(x))# 产生随机测量值，数据不相关
# y2 = 5+np.exp(x)# 产生强相关随机数据
# ax1 = plt.subplot(121)
# plt.scatter(x,y1, color='#95d0fc',alpha=0.3,edgecolors='#ff81c0',label='no correl')
# plt.xlabel('no correlation')
# plt.xlim(-4,4,2)
# plt.ylim(-5,25,5)
# plt.grid(True)
# plt.legend(loc=2)
# ax2 = plt.subplot(122,sharey=ax1,sharex=ax1)#?
# plt.scatter(x,y2, color='#95d0fc',alpha=0.3,edgecolors='#ff81c0',label='correl')
# plt.xlabel('stronger correlation')
# plt.xlim(-4,4,2)
# plt.ylim(-5,25,5)
# plt.grid(True)
# plt.legend(loc=1)
# plt.show()
