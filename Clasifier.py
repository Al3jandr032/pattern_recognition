import numpy as np
from math import sqrt,pow,pi,exp
from numpy.linalg import inv,det

def average(numArray):
		res = np.zeros( (numArray.shape[0],1) )
		index = 0
		for dim in numArray:
			avg = 0.0
			for element in dim:
				avg += element
			avg = avg/dim.size
			res[index] = avg
			index += 1
		return res

class EuclideanDistance(object):
	"""docstring for eculedianDistance"""
	def __init__(self):
		super(EuclideanDistance, self).__init__()

	def distance(self,x,c):
		avg = average(c)
		tmp = 0.0
		if avg.shape[0] == x.shape[0]:
			for i in range(0,x.shape[0]):
				tmp += pow(x[i]-avg[i],2)
		return sqrt(tmp)

	def distanceToPoint(self,x,c,_class=None):
		tmp = 0.0
		if c.shape[0] == x.shape[0]:
			for i in range(0,x.shape[0]):
				tmp += pow(x[i]-c[i],2)
		return sqrt(tmp)

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

	def distanceToPoint(self,p,c,_class):
		covarianza = self.covariantMatrix(_class)
		xminusAvg = p-c
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

	def __init__(self,k=3, index=0):
		super(KNN, self).__init__()
		self.k = k
		self.clasifiers = [EuclideanDistance(),Mahalanobis(),MaxProbability()]
		self.index = index

	def keywithmaxval(self,d):
	     	v=list(d.values())
     		k=list(d.keys())
	     	return k[v.index(max(v))]

	def distance(self,x,_classes):
		#print "knn-distance type of x: ",type(x)
		lst = [	]
		index = 0
		
		for cl in range(0,len(_classes)):
			for dim in range(0,_classes[cl].shape[1]):
				tmp_list = []
				for axis in range(0,_classes[cl].shape[0]):
					tmp_list.append([_classes[cl][axis][dim]])
				p = np.array(tmp_list)
				#print p
				temp = {"distance":self.clasifiers[self.index].distanceToPoint( x,p,_classes[cl]),"class":cl,"index":index}
				lst.append( temp)
				index += 1
		lst.sort(key=lambda x: x['distance'], reverse=False	)
		knn = lst[:self.k]

		result = {}
		for cl in knn:
			#print "clase : {} , mean : {} ".format(cl['index']+1,cl['distance'])
			result[cl['class']+1] = 0
		for cl in knn:
			#print "clase : {} , mean : {} ".format(cl['index']+1,cl['distance'])
			result[cl['class']+1] += 1
		"""
		for key, value in result.iteritems():
			print "key : {} , value : {}".format(key,value)
		"""
		
		return self.keywithmaxval(result)
