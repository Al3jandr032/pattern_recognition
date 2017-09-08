#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import sys
import numpy as np 
from math import sqrt,pow,pi,exp
from numpy.linalg import inv,det
import matplotlib.pyplot as plt
from generator import ClassGenerator
from generator import ClassHolder
from generator import Validator
from Clasifier import EculedianDistance
from Clasifier import KNN

if __name__ == '__main__':
	if len(sys.argv) > 1:
		numPopulation = int(sys.argv[1])
		path_file = sys.argv[2]
		a = ClassGenerator(size=int(numPopulation),config_path=path_file)
		holder = ClassHolder(a.generate())
		numOfClases = holder.getNumClasses()
		print "number of clases : ",numOfClases
		v = Validator(holder, int(sys.argv[3]) )
		preformance = []
		rest_matrix = []
		for i in range(0,numOfClases):
			rest_matrix.append(v.check(i,False))

		average = 0.0
		for i in range(0,numOfClases):
			print rest_matrix[i]
			average += rest_matrix[i][i+1]
		tmp = (average*100)/(numPopulation*numOfClases)
		preformance.append(tmp)
		print "restit method result : {}".format(tmp)

	
		cross_total = 0.0
		for times in range(0,20):
			matrix = []
			for i in range(0,numOfClases):
				matrix.append(v.check(i,True))

			average = 0.0
			for i in range(0,numOfClases):
				print matrix[i]
				average += matrix[i][i+1]
			tmp = (average*100)/((numPopulation*numOfClases)/2)
			print tmp
			cross_total += tmp
		preformance.append(cross_total/20)
		print "cross method result : {}".format(cross_total/20)
		_total = 0.0
		for x in preformance:
			_total += x
		print "El performance total es : {}".format(_total/len(performance))
	
	else:
 		print "Filename required"

#if holder.classify(KNN(150,1),x,y,l):
#	plt.show()
	#pass
