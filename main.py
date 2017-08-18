import numpy as np 
from generator import ClassGenerator
from generator import ClassHolder

numClass = raw_input("introduce el numero de clases :")
numPopulation = raw_input("introduce el numero de representantes :")
a = ClassGenerator(numClass,numPopulation)
#for i in a.generate():
#	print i
holder = ClassHolder(a.generate())
holder.classify()
"""
holder.addClass(np.array([[1,3,1,2,3],[2,5,5,2,3]]))
holder.addClass(np.array([[6,6,7,8,8],[4,3,4,4,5]]))
holder.addClass(np.array([[10,12,10,15,10],[11,11,13,14,12]]))
holder.addClass(np.array([[1,3,1,2,3],[11,8,10,8,9]]))
holder.addClass(np.array([[6,6,7,8,8],[8,10,12,7,8]]))

"""

