import numpy as np
from numpy.linalg import inv

#c1 = np.array([[-1,1,-1,0,1],[-1.4,1.6,1.6,-1.4,-0.4]])
#c2 = np.array([[-1,-1.4],[1,1.6],[-1,1.6],[0,-1.4],[1,-0.4]])

c1 = np.array([[-1.0,-1.0,0,1.0,1.0],[0,-1.0,0,0,1.0]])
c2 = np.array([[-1.0,0],[-1.0,-1.0],[0,0],[1.0,0],[1.0,1.0]])
x = np.array([[4],[3]])

mean = np.array([[7],[2]])



def variantMatrix(c1,c2,n):
	d = np.dot(c1,c2)
	for x in range(0,len(d)):
		for i in range(0,len(d[x])):
			d[x][i]=d[x][i]/n
	return inv(d)


a = variantMatrix(c1,c2,len(c1[0]))		
tmp = x-mean

b = np.dot(a,tmp)

aux1 = np.dot(tmp.transpose(),b)
print aux1

#print tmp.transpose()

