import numpy as np
from numpy.linalg import inv

def average(numArray):
		res = np.zeros( (len(numArray),1) )
		index = 0
		for dim in numArray:
			avg = 0.0
			for element in dim:
				avg += element
			avg = avg/dim.size
			res[index] = avg
			index += 1
		return res

def covariantMatrix(mean,c1):
	d = np.dot(c1,c1.transpose())
	n = len(c1[0])
	for x in range(0,len(d)):
		for i in range(0,len(d[x])):
			d[x][i]=d[x][i]*1/n
	return inv(d)

def divBy(d,n):
	for x in range(0,len(d)):
		for i in range(0,len(d[x])):
			d[x][i]=float(d[x][i])/float(n)
	return d

def mahalanobis(c1,x):
	
	a = covariantMatrix(c1)		
	#print a
	tmp = x-mean
	print tmp
	b = np.dot(a,tmp)

	aux1 = np.dot(tmp.transpose(),b)
	return aux1[0][0]


#c1 = np.array([[1.0,3.0,1.0,2.0,3.0],[2.0,5.0,5.0,2.0,3.0]])
#c2 = np.array([[6.0,6.0,7.0,8.0,8.0],[4.0,3.0,4.0,4.0,5.0]])

#c1 = np.array([[-1.0,-1.0,0,1.0,1.0],[0,-1.0,0,0,1.0]])
#c2 = np.array([[-1.0,0],[-1.0,-1.0],[0,0],[1.0,0],[1.0,1.0]])

c1 = np.array([[0,1.0,1.0,1.0],[0,0,1.0,0],[0,0,0,1.0]])
c2 = np.array([[0,1.0,0,0],[1.0,1.0,1.0,0],[0,1.0,1.0,1.0]])
p = np.array([[4],[5],[0]])

#_sum=c1-average(c1)	
#print divBy(np.dot(_sum,_sum.transpose()))
_sum=c2-average(c2)	
#print np.dot(_sum,_sum.transpose())
covarianza = divBy(np.dot(_sum,_sum.transpose()),len(_sum[0]))
xminusAvg = p-average(c2)

tmp = np.dot(covarianza,xminusAvg)
print np.dot(xminusAvg.transpose(),tmp)
"""
#print mahalanobis(c1,p)
#print average(c1)

#print tmp.transpose()
"""

