cd
import numpy as np
import pylab as plt

def IntegrateEnergy():
	dmu=0.001
	int1=np.zeros(1/dmu)
	int2=np.zeros(1/dmu)
	for x in range(0,int1.size):
		mu1=x/int1.size+0.000001#avoid dividing by zero
		mu2=-1.0+x/int2.size+0.000001
		int1=np.exp(1/mu1)*dmu
		int2=np.exp(1/mu2)*dmu
	return (np.sum(int1),np.sum(int2))

def IntegrateFlux():
	dmu=0.001
	int1=np.zeros(1/dmu)
	int2=np.zeros(1/dmu)
	for x in range(0,int1.size):
		mu1=x/int1.size+0.00001
		mu2=-1+x/int2.size+0.00001
		int1=np.exp(1/mu1)*mu1*dmu
		int2=np.exp(1/mu2)*mu2*dmu
	return (np.sum(int1), np.sum(int2))
			
if __name__ == "__main__":
	z=np.arange(0,1,0.001)
	EnergyDensity=np.zeros((z.size,5))
	Flux=np.zeros((z.size,5))
	tau=(0.01,0.1,1,10,100)
	Integral1,Integral2,FluxIntegral1,FluxIntegral2=np.zeros(5),np.zeros(5),np.zeros(5),np.zeros(5)
	for x in range(0,5):
		Integral1[x],Integral2[x]=IntegrateEnergy()
		FluxIntegral1[x],FluxIntegral2[x]=IntegrateFlux()
		for y in range(0,z.size):	
			EnergyDensity[y,x]=(2.0-(np.exp(-tau[x]*z[y])*Integral1[x]+np.exp(-tau[x]*(1.0-z[y]))*Integral2[x]))
			Flux[y,x]=np.exp(-tau[x]*(1.0-z[y]))*FluxIntegral2[x]-np.exp(-tau[x]*z[y])*FluxIntegral1[x]
	fig=plt.figure()
	#plt.semilogx()
	plt.ylabel(r'$\frac{c u_{\nu}}{2 \pi B_{\nu}(T)}$')	
	plt.xlabel(r'$z$')
	plt.title('Ex 2.3')
	plt.plot(z,EnergyDensity)
	plt.legend((r'$\tau_0=0.01$',r'$\tau_0=0.1$',r'$\tau_0=1$',r'$\tau_0=10$',r'$\tau_0=100$'), loc=2)
	fig.savefig('em1-2-3.png')	
	fig.clear()
	plt.ylabel(r'$\frac{F_\nu}{2 \pi B_{\nu}(T)}$')	
	plt.xlabel(r'$z$')
	plt.title('Ex 2.4')
	plt.plot(z,Flux)
	plt.legend((r'$\tau_0=0.01$',r'$\tau_0=0.1$',r'$\tau_0=1$',r'$\tau_0=10$',r'$\tau_0=100$'), loc='lower right')
	plt.savefig('em1-2-4.png')	
	#plotting \frac{c u_\nu}{2 \pi B_\nu(T)}=2-Exp[z]\int_0^1Exp[tau/mu dmu - Exp[1-z]\int_-1^0 Exp[tau/mu dmu

