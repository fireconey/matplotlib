# 绘制维图
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import numpy as np
fig=figure(figsize=(10,10),dpi=100)
ax=Axes3D(fig)
x=np.arange(-4,4,0.25)
y=np.arange(-4,4,0.25)
x,y=np.meshgrid(x,y)

r=np.sqrt(x**2+y**2)
z=np.sin(r)
# rstride,cstride表示网格的宽度
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap="hot")
savefig("faf.png",dpi=100)
show()