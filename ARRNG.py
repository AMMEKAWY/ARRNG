import numpy as np

e_ion=15.8
e_exc=11.6

def fn(l):

	return(np.exp(-l/e_ion)*(1-np.exp(-l/e_exc)))


#def rand(e):
	



	
def rand(e):

	x=np.random.uniform(0,e)
	y=np.random.uniform(0,1)	

	while True:
		
		if(fn(x)>y):
		
			return(x)
			break
			
		else:
		
			x=np.random.uniform(0,e)
			#y=np.random.uniform(0,1)
