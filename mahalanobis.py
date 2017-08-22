import numpy as np
from numpy.linalg import inv

#c1 = np.array([[-1,1,-1,0,1],[-1.4,1.6,1.6,-1.4,-0.4]])
#c2 = np.array([[-1,-1.4],[1,1.6],[-1,1.6],[0,-1.4],[1,-0.4]])

c1 = np.array([[-1.0,-1.0,0,1.0,1.0],[0,-1.0,0,0,1.0]])
c2 = np.array([[-1.0,0],[-1.0,-1.0],[0,0],[1.0,0],[1.0,1.0]])
x = np.array([[4],[3]])
mean = np.array([[7],[2]])




a = np.dot(c1,c2)		

def variantMatrix(d,n):
	for x in range(0,len(d)):
		for i in range(0,len(d[x])):
			d[x][i]=d[x][i]/n
	return inv(d)


aux = variantMatrix(a,5)		
print aux
tmp = x-mean
print tmp
print tmp.transpose()
print tmp*aux*tmp.transpose()

