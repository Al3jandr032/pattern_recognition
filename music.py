#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
from generator import *
import numpy as np 
from math import sqrt,pow,pi,exp
from numpy.linalg import inv,det
import matplotlib.pyplot as plt
from generator import ClassGenerator
from classholder import ClassHolder
from Clasifier import EuclideanDistance
from Clasifier import KNN



gen = h5fGenerator(config_path="proyecto/")
data = gen.load()

"""
print "introduce 0 para usar distancia euclediana"
print "introduce 1 para usar distancia mahalanobis"
metodo = raw_input("Metodo: ")
num = raw_input("Numero de vecinos: ")

"""
holder = ClassHolder(gen.load())



def test():
	for cl in xrange(4):
		for cont in xrange(50):
			arraylist = []
			for i in data[cl][:,cont]:
				arraylist.append([i])
			#print arraylist
			#holder.classify(KNN(3,1),arraylist,20)
			holder.classify(MaxProbability(),arraylist,20)
			#break
		#break
		print "%%%%%%%%%%%%%%%%%%%%%%%%%%%"
#holder.classify(MaxProbability(),0,0,20)
test()


