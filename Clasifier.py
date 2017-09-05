import numpy as np 
from math import sqrt,pow,pi,exp
from numpy.linalg import inv,det

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
	
	def distance(self,x,c):
		avg = average(c)
		return sqrt(pow(x[0]-avg[0],2)+pow(x[1]-avg[1],2))
		
class Mahalanobis(object):
	"""docstring for mahalanobis"""
	def __init__(self):
		super(Mahalanobis, self).__init__()
	
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

class MaxProbability(object):
	"""docstring for MaxProbability"""
	def __init__(self):
		super(MaxProbability, self).__init__()
	
	def covariantMatrix(self,c):
		_sum=c-average(c)	
		return self.divBy(np.dot(_sum,_sum.transpose()),len(_sum[0]))

	def divBy(self,d,n):
		for x in range(0,len(d)):
			for i in range(0,len(d[x])):
				d[x][i]=float(d[x][i])/float(n)
		return d

	def divBy2(self,d,n):
		for x in range(0,len(d)):
			for i in range(0,len(d[x])):
				d[x][i]=-1*float(d[x][i])/2
		return d

	def distance(self,p,c):
		covarianza = self.covariantMatrix(c)
		xminusAvg = p-average(c)
		tmp = np.dot(covarianza,xminusAvg)
		mahalanubis= np.dot(xminusAvg.transpose(),tmp)
		#print mahalanubis[0][0]
		a = exp(mahalanubis[0][0]*-0.5)
		b = pow(pi*2,float(3/2))
		c = det(covarianza)
		d = a/pow(c,-0.5)*b
		return d


class KNN(object):
	
	def __init__(self,k , index):
		super(KNN, self).__init__()
		self.k = k
		self.clasifiers = [EculedianDistance(),Mahalanobis(),MaxProbability()]
		self.index = index

	def distance(self,x,_classes):
		lst = [	]
		index = 0
		for i in _classes:
			temp = {"distance":self.clasifiers[self.index].distance( x,i ),"class":i,"index":index}
			lst.append( temp)
			index += 1
		
		lst.sort(key=lambda x: x['distance'], reverse=False	)
		
		

		#for cl in lst:
		#	print "clase : {} , mean : {} ".format(cl['index']+1,cl['distance'])
		knn = lst[:self.k]
		result = {}
		for cl in knn:
			print "clase : {} , mean : {} ".format(cl['index']+1,cl['distance'])
			result[cl['index']+1] = 0

		for cl in knn:
			result[cl['index']+1] += 1

		print result

		#print lst[0]['avg']," : ",limit
		print "return : ",1+lst[0]['index']
		return 1+lst[0]['index']