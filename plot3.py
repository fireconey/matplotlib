# 1、设定图片边界
# 2、设置自定意义的横坐标的符号
# 3、移动边框（四边形的）隐藏其余的边框
# 4、添加图例
# 5、曲线上某点的说明
from matplotlib.pylab import *
import numpy as np
# 创建一个8x6的点图(图像的大小)，分辨率为80
figure(figsize=(8,6),dpi=80)

# 创建一个1X1的子图放在图样中的第一块（这里就一块）
subplot(1,1,1)

x=np.linspace(-np.pi,np.pi,256,endpoint=True)
s,c=cos(x),sin(x)


# 设置x轴的上下线
xlim(x.min()*1.1,x.max()*1.1)

# 设置x轴的记号()
# xticks(np.linspace(-4,4,10,endpoint=True))
# 不用具体的数值，自己标记
xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
       [r"$-\pi$",r"$-\pi/2$",r"$0$",r"$+\pi/2$",r"$+\pi$"])

# 设置y轴的记号
yticks([-1,0,+1])
savefig("plot.png",dpi=100)

# 隐藏边框
ax=gca()
# ax.spines["right"].set_color("none")
# ax.spines["top"].set_color("none")
# 设置标记在坐标线的上还是下边
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

# 移动边框（data，0）表示数据空间的0点
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))

# 添加图例
# plot(x,s,color="blue",linewidth=1,linestyle="-")
plot(x,c,color="red",linewidth=1,linestyle="-",label="cos")
plot(x,s,color="blue",linewidth=1,linestyle="-",label="sin")

# 图例还要设置位置（10个位置）
legend(loc=1)

# 曲线上某点的说明
t=2*np.pi/3
plot([t,t],[0,np.cos(t)],color="blue",linewidth=2,linestyle="--")#画点是两个坐标范围动，下为动一个
# 曲线上点的注释frac表示分子。xy表示注释点的位置,xytext表示注释的位置
annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',xy=(t,np.cos(t)),

	xytext=(+1,-1),
	fontsize=16,
	arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-0.9")
   
	)
show()
