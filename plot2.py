from matplotlib.pylab import *
import numpy as np
# 创建一个8x6的点图(图像的大小)，分辨率为80
figure(figsize=(8,6),dpi=80)

# 创建一个1X1的子图放在图样中的第一块（这里就一块）
subplot(1,1,1)

x=np.linspace(-np.pi,np.pi,256,endpoint=True)
s,c=cos(x),sin(x)
plot(x,s,color="blue",linewidth=1,linestyle="-")
plot(x,c,color="red",linewidth=10,linestyle="-")


# 设置x轴的上下线
xlim(-4,4)

# 设置x轴的记号()
xticks(np.linspace(-4,4,10,endpoint=True))
savefig("plot.png",dpi=1080)
show()
