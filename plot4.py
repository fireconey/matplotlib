# 散点图
from matplotlib.pylab import *
import numpy as np
n=1024
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
t=np.arctan2(x, y)
# c表示颜色(可以变得)，s表示大小（可以变的） alpha表示透明
scatter(x,y,c=t)
show()