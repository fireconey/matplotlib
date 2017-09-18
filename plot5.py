# 柱状图
from matplotlib.pylab import *
import numpy as np
n=12
x=np.arange(n)
y1=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
y2=(1-x/float(n))*np.random.uniform(0.5,1.0,n)

bar(x,+y1,facecolor="blue",edgecolor="white")
bar(x,-y2,facecolor="red",edgecolor="white")

# x+0.4是以柱状图为基准，后移多少
for j,y in zip(x,y1):
	text(j+0.4,y+0.05,"%0.2f" %y ,ha="center",va="bottom")

# for 的zip中字母和外面的不能一致，会报错。
# 前面两个参数是位置，后面参数是标志。后面的是原点
for j,y in zip(x,y2):
	text(j+0.4,-y-0.05,"%0.2f" %-y ,ha="center",va="top")

ylim(-1.25,+1.25)
show()