#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import numpy as np 
from math import sqrt,pow,pi,exp
from numpy.linalg import inv,det
import matplotlib.pyplot as plt
from generator import ClassGenerator
from generator import ClassHolder
from generator import Validator
from Clasifier import EculedianDistance
from Clasifier import KNN


numPopulation=100
path_file="clases.ini"
a = ClassGenerator(size=numPopulation,config_path=path_file)
holder = ClassHolder(a.generate())
#x = raw_input("Coordenada x: ")
#y = raw_input("Coordenada y: ")
v = Validator(holder,0)
l = 20
for i in range(0,4):
	print v.check(i,True)
for i in range(0,4):
	print v.check(i,False)

#if holder.classify(KNN(150,1),x,y,l):
#	plt.show()
	#pass
