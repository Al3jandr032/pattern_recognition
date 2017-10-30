import numpy as np 
from math import sqrt,pow
import matplotlib.pyplot as plt
import time

x = np.linspace(0,2*np.pi,50)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x-(np.pi/2))

fig = plt.figure(figsize=(10,3))
ax = fig.add_subplot(1,1,1)
ax.plot(x,y1,'-o',color='red',label='$sin(\omega t)$')
ax.plot(x,y2,'o-',color='blue',label='$cos(\omega t)$')
ax.plot(x,y3,'^',color='green',label='$sin(\omega t -\pi/2)$',markersize=10)

#ax.vline(x=[0,np.pi,2*np.pi],ymin=3,ymax=3, linestyles='--',alpha=0.5)
ax.set_ylim((-1.1,1.1))
ax.set_xlim((-0.1,6.4))
ax.set_xlabel('$t$')
ax.set_xlabel('$f(t)$')
#ax.set_xticks(np.linspace(0,2* np.pi,5))
#ax.set_yticks(np.linspace(0,2* np.pi,5))
ax.grid()
fig.show()
time.sleep(5)