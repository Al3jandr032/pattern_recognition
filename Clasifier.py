from math import sqrt,pow
from numpy.linalg import inv

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

class EculedianDistance(object):
	"""docstring for eculedianDistance"""
	def __init__(self):
		super(EculedianDistance, self).__init__()
	
	def distance(self,avg1,avg2):
		return sqrt(pow(avg1[0]-avg2[0],2)+pow(avg1[1]-avg2[1],2))
		
class mahalanobis(object):
	"""docstring for mahalanobis"""
	def __init__(self):
		super(mahalanobis, self).__init__()
	
	def covariantMatrix(self,c):
		_sum=c-average(c)	
		return self.divBy(np.dot(_sum,_sum.transpose()),len(_sum[0]))

	def divBy(self,d,n):
		for x in range(0,len(d)):
			for i in range(0,len(d[x])):
				d[x][i]=float(d[x][i])/float(n)
		return d

	def distance(self,p,c):
		covarianza = self.covariantMatrix(c)
		xminusAvg = p-average(c)
		tmp = np.dot(covarianza,xminusAvg)
		return np.dot(xminusAvg.transpose(),tmp)
		
