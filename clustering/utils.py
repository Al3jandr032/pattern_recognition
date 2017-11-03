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
		#avg = average(c)
		tmp = 0.0
		if c.shape[0] == x.shape[0]:
			for i in range(0,x.shape[0]):
				tmp += pow(x[i]-c[i],2)
		return sqrt(tmp)

	def distanceToPoint(self,x,c,_class=None):
		tmp = 0.0
		if c.shape[0] == x.shape[0]:
			for i in range(0,x.shape[0]):
				tmp += pow(x[i]-c[i],2)
		return sqrt(tmp)
