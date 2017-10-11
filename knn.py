#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import numpy as np 
from math import sqrt,pow,pi,exp
from numpy.linalg import inv,det
import matplotlib.pyplot as plt
from generator import ClassGenerator
from generator import ClassHolder
from Clasifier import EuclideanDistance
from Clasifier import KNN


numPopulation=100
path_file="clases.ini"
a = ClassGenerator(size=numPopulation,config_path=path_file)
holder = ClassHolder(a.generate())
holder.plot()
print "introduce 0 para usar distancia euclediana"
print "introduce 1 para usar distancia mahalanobis"
metodo = raw_input("Metodo: ")
metodo = int(metodo)
x = raw_input("Coordenada x: ")
y = raw_input("Coordenada y: ")
num = raw_input("Numero de vecinos: ")
while int(num)%2 == 0:
	num = raw_input("Numero de vecinos: ")
holder.classify(KNN(int(num),metodo),x,y,20)
holder.plot(x,y)
end = raw_input("terminar enter")
