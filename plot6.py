# 等高线
import numpy as np
from matplotlib.pylab import *
def f(x,y): return(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)

# meshgrid 是产生两个二维矩阵
x,y=np.meshgrid(x,y)
# 绘制二维云图，pcolor 对等高线填色，contour3绘制三维图
contourf(x,y,f(x,y),8,alpha=.75,cmap="jet")
# 绘制二维等高线
contour(x,y,f(x,y),8,colors="black",linewidth=1)
show()
print(x)
print(y)