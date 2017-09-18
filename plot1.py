# encoding:utf-8
from matplotlib.pylab import *
import numpy as np
# -pi 到pi共256个数据，其中endpoint 表示是否包括尾数
# 就是累加后是否到指定的最后一个数
x=np.linspace(-np.pi, np.pi,256,endpoint=True)
c,s=np.cos(x) ,np.sin(x)

#由于使用的import*所以不用plt.plot
plot(x,c)
plot(x,s)
show()