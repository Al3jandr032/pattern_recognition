import sys
import time
import numpy as np 
import matplotlib.pyplot as plt
from generator import ClassGenerator
from generator import ClassHolder
from Clasifier import EculedianDistance

#numClass = raw_input("introduce el numero de clases :")
#numPopulation = raw_input("introduce el numero de representantes :")
#a = ClassGenerator(size=numPopulation,config_path="clases.ini")
#print a.generate()

#holder = ClassHolder(a.generate())
#holder.classify(eculedianDistance)
"""
holder.addClass(np.array([[1,3,1,2,3],[2,5,5,2,3]]))
holder.addClass(np.array([[6,6,7,8,8],[4,3,4,4,5]]))
holder.addClass(np.array([[10,12,10,15,10],[11,11,13,14,12]]))
holder.addClass(np.array([[1,3,1,2,3],[11,8,10,8,9]]))
holder.addClass(np.array([[6,6,7,8,8],[8,10,12,7,8]]))

"""

if __name__ == '__main__':
	if len(sys.argv) > 1:
		numPopulation = sys.argv[1]
		path_file = sys.argv[2]
		a = ClassGenerator(size=numPopulation,config_path=path_file)
		holder = ClassHolder(a.generate())
		x = raw_input("Coordenada x: ")
		y = raw_input("Coordenada y: ")
		l = raw_input("Limite : ")
		if holder.classify(EculedianDistance(),x,y,l):
			plt.show()
	else:
 		print "Filename required"

