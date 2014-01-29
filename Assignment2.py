import numpy as np
import matplotlib.pylab as plt

def m(r):
	k = 963512 # m_sol/pc
	M_0 =3700000 # m_sol/pc
	m = k*r + M_0
	return m
def v(r): #takes r in pc, returns v in km/s
	k = 963512 # m_sol/pc
	M_0 = 3700000 # m_sol/pc
	G = 4.60e-30 # pc^3 s^-2 m_sol^-1
	con= 1/3.08e13 #pc to km
	v = np.sqrt(G*(k+M_0/r)) #in pc
	v = v*con #need km/s
	return v

r1=np.arange(0.01,1000,0.01) # pc

fig = plt.figure(figsize = (8, 8))
fig.suptitle(r'$Carrol\; &\; Ostlie,\; 24.36\; d,\;e$')
ax1 = fig.add_subplot(2,1,1)
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.set_ylabel(r'$Log(M_r)\; (\mathrm{M_\odot})$')
ax1.set_xlabel(r'$Log(r)\; (\mathrm{pc})$')
ax1.plot(r1, m(r1))

ax2 = fig.add_subplot(2,1,2)
ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.set_ylabel(r'$Log(v)\; (\mathrm{km\; s^{-1}})$')
ax2.set_xlabel(r'$Log(r)\; (\mathrm{pc})$')
ax2.plot(r1,v(r1))
plt.savefig('Assignment2.png')
