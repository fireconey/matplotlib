# encoding:utf-8
from matplotlib.pylab import *
import numpy as np
# -pi ��pi��256�����ݣ�����endpoint ��ʾ�Ƿ����β��
# �����ۼӺ��Ƿ�ָ�������һ����
x=np.linspace(-np.pi, np.pi,256,endpoint=True)
c,s=np.cos(x) ,np.sin(x)

#����ʹ�õ�import*���Բ���plt.plot
plot(x,c)
plot(x,s)
show()