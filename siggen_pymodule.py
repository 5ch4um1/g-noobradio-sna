# this module will be imported in the into your flowgraph


f1 = 60000000
f2 = 1000000000

f = f1

step = 500000

tb = siggen()

def sweeper(arg):
	global f1,f2,f,step
	if arg:
		f +=step
	if f>= f2:f=f1 
	      
		

	return f	
	
