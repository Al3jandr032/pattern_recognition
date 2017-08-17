import numpy as np 
from math import sqrt,pow
import matplotlib.pyplot as plt

classes = []
classes.append(np.array([[1,3,1,2,3],[2,5,5,2,3]]))
classes.append(np.array([[6,6,7,8,8],[4,3,4,4,5]]))
classes.append(np.array([[10,12,10,15,10],[11,11,13,14,12]]))
 
x = np.array([[-3],[18]])

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

def eculedianDistance(avg1,avg2):
	return sqrt(pow(avg1[0]-avg2[0],2)+pow(avg1[1]-avg2[1],2))


#for _class in classes:
#	print eculedianDistance(x,average(_class))

fig = plt.figure()
ax = fig.add_subplot(111)

for _class in classes:
	ax.scatter(_class[0], _class[1], color='darkgreen', marker='.')
#ax.plot(a, b, color='lightblue', linewidth=3)
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
plt.show()
