import numpy as np
import pylab as plt

# 2.2
# Need to integrate 2pi B_\nu(t) \int_-1^1(1-Exp(-tau/mu)mu dmu
# plot F_\nu/(pi B_\nu)

def IntegrateFlux(tau):
	dmu=0.001
	tmp = np.zeros(2/dmu)
	for x in range(0,1001):
		mu=x/1000.0+0.00000001
		tmp[x]=(1-np.exp(-tau*mu))*mu*dmu
	return sum(tmp)
	

if __name__ == "__main__":
#For each tau in [0.01,100], need to integrate \int_0^1(1-Exp(-tau/mu)mu dmu.
	Flux=np.zeros(10001)
	tau=np.zeros(10001)
	for x in range(0,10001):
		tau[x]= 0.01+100.0*x/10000.0
		Flux[x]=2*IntegrateFlux(tau[x])
	fig=plt.figure()
	plt.semilogx()
	plt.ylabel(r'$\frac{F_\nu}{\pi B_\nu}$')
	plt.xlabel(r'$\tau_0$')
	plt.title('Ex 2.2')
	plt.axis([0.01,100,0,1.2])
	plt.axhline(y=1,xmin=0.001,xmax=100,color='k',ls='--')
	plt.text(0.1,1.0,r'$F_\nu=\pi B_\nu$')
	plt.plot(tau,Flux)
	fig.savefig('test..png')
#
