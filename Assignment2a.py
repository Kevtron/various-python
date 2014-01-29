import numpy as np
import pylab as plt

V=np.array([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
log10Am=np.array([-2.31,-1.71,-1.11,-0.51,0.09,0.69,1.29,1.89,2.24,2.59,2.94,3.29,3.89,4.49,5.09,5.69])

V1=V[:8]
Am1=log10Am[:8]
V2=V[12:]
Am2=log10Am[12:]
t1=np.arange(4,20,0.1)
slope1,intercept1=np.polyfit(V1,Am1,1)
slope2,intercept2=np.polyfit(V2,Am2,1)
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(1,1,1)
ax.set_xlabel(r'$V$')
ax.set_ylabel(r'$Log_{10}(A_m)$')
ax.plot(V, log10Am, 'b*')
ax.plot(t1,slope1*t1+intercept1,'r-')
ax.plot(t1,slope2*t1+intercept2,'g-')
plt.title(r'$C&O\;24.7$')
plt.text(6,6,r'$Log_{10}Am=$%1.2f$V+$%1.2f'%(slope1, intercept1),color='r')
plt.text(12,-2,r'$Log_{10}Am=$%1.2f$V+$%1.2f'%(slope2, intercept2),color='g')
plt.savefig('Assignment2a.png')
