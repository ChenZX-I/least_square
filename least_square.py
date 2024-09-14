# 最小二乘法自动计算与生成图像
import numpy as np
import matplotlib.pylab as pl

# y = b*x + a
y = [1.800, 1.280, 0.990, 0.600, 0.520] #请手动填入此数值
x = [8.216, 7.410, 6.882, 5.492, 5.196] #请手动填入此数值
nx = len(x)
ny = len(y)
b = 0
a = 0

# 计算均值
averx = 0
avery = 0
for xi in x:
    averx += xi

averx = averx / nx

for yi in y:
    avery += yi

avery = avery / ny

# 计算各参数
numerator = 0 # 分子
denominator = 0 # 分母
for i in range(0, nx):
    numerator += (x[i] - averx) * (y[i] - avery)
    denominator += (x[i] - averx)**2
    
b = numerator / denominator
a = avery - averx * b
print('a = ',a)
print('b = ',b)

# 构造二乘法方程
X = np.linspace(5.14, 8.20, 100)  #请手动改此数值
Y = b * X + a

# 画图
pl.rc('font' , family = 'SimHei')      #用来正常显示中文字符
pl.rc('font' , size = 16)              #设置显示字体的大小
pl.plot(x, y, '-*b', label = '折线图')
pl.plot(X, Y, '--r', label = '二乘法方程')
pl.xlabel('v/(x10^4Hz)')    # x轴标签
pl.ylabel('U0/V')    # y轴标签
pl.legend()
pl.grid()
pl.show()
