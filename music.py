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

class MusicGenClass(object):
	"""docstring for MusicGenClass"""
	def __init__(self, path="proyecto/"):
		gen = h5fGenerator(config_path=path)
		self.data = gen.load()
		self.holder = ClassHolder(gen.load())
		

	def classify(self):
		for cl in xrange(4):
			average =0
			for cont in xrange(50):
				arraylist = []
				for i in self.data[cl][:,cont]:
					arraylist.append([i])
				print arraylist
				_class = self.holder.classify(KNN(3,0),arraylist,0)
				print _class," : ",cl,(cl+1 == _class)
				if(cl+1 == _class):
					average += 1
				#holder.classify(MaxProbability(),arraylist,20)
				break
			break
			print "aciertos : {}".format(average)
			print "%%%%%%%%%%%%%%%%%%%%%%%%%%%"

	def process(self, arraylist):
		_class = self.holder.classify(KNN(3,0),arraylist,0)
		return _class
#holder.classify(MaxProbability(),0,0,20)

"""
print "introduce 0 para usar distancia euclediana"
print "introduce 1 para usar distancia mahalanobis"
metodo = raw_input("Metodo: ")
num = raw_input("Numero de vecinos: ")

"""



"""
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
"""
m= MusicGenClass()
m.classify()

