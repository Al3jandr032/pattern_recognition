from math import sqrt,pow

def eculedianDistance(avg1,avg2):
		return sqrt(pow(avg1[0]-avg2[0],2)+pow(avg1[1]-avg2[1],2))

def average(numArray):
		res = np.zeros( (numArray.ndim,1) )
		index = 0
		for dim in numArray:
			avg = 0.0
			for element in dim:
				avg += element
			avg = avg/dim.size
			res[index] = avg
			index += 1
		return res

def covariantMatrix(c1,c2,n):
	d = np.dot(c1,c2)
	for x in range(0,len(d)):
		for i in range(0,len(d[x])):
			d[x][i]=d[x][i]/n
	return inv(d)

def mahalanobis(c1,x):
	c2 = c1.transpose()
	a = covariantMatrix(c1,c2,len(c1[0]))		
	print a
	tmp = x-mean
