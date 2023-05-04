
import numpy as np

e_ion=15.8
e_exc=11.6

def fn(l):

	#return(np.exp(-e_ion/l))*(1-np.exp(-l/e_exc))
	return(np.exp(-l/e_exc))

#def rand(e):
	

	
def rand(e):

	x=np.linspace(10**-12,e,10000)
	y=fn(x)

	i=np.random.randint(0, e)
	z=np.random.randint(0, 1)
	
	while True:
		
		if(y[i]>z):
		
			return(x[i])
			break
			
		else:
		
			z=np.random.randint(0, 1)
			#y=np.random.uniform(0,1)
			
z=rand(20)
print(z)
