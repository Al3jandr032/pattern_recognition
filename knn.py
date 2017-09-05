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
x = 4
y = 5
l = 20
if holder.classify(KNN(3,0),x,y,l):
	#plt.show()
	pass
	