#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import numpy as np 
from math import sqrt,pow,pi,exp
from numpy.linalg import inv,det
import matplotlib.pyplot as plt
from generator import ClassGenerator
from generator import ClassHolder
from Clasifier import EuclideanDistance


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
		b = pow(pi*2,float(c.ndim/2))
		c = det(covarianza)
		d = a/pow(c,-0.5)*b
		print "P :",d
		return d

numPopulation=100	
path_file="clases.ini"
a = ClassGenerator(size=numPopulation,config_path=path_file)
holder = ClassHolder(a.generate())
x = 4
y = 5
l = 20
if holder.classify(MaxProbability(),x,y,l):
	#plt.show()
	pass
	