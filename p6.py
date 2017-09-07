#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import numpy as np 
from math import sqrt,pow,pi,exp
from numpy.linalg import inv,det
import matplotlib.pyplot as plt
from generator import ClassGenerator
from generator import ClassHolder
from Clasifier import EculedianDistance
from Clasifier import KNN


numPopulation=100
path_file="clases.ini"
a = ClassGenerator(size=numPopulation,config_path=path_file)
holder = ClassHolder(a.generate())
#x = raw_input("Coordenada x: ")
#y = raw_input("Coordenada y: ")
l = 20
c1 = holder.getClass(1)

c2 = holder.getSample(1)
print holder.getElements(1,True)

#if holder.classify(KNN(150,1),x,y,l):
#	plt.show()
	#pass
