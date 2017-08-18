import numpy as np 
from math import sqrt,pow
import matplotlib.pyplot as plt

classes = []
classes.append(np.array([[1,3,1,2,3],[2,5,5,2,3]]))
classes.append(np.array([[6,6,7,8,8],[4,3,4,4,5]]))
classes.append(np.array([[10,12,10,15,10],[11,11,13,14,12]]))
classes.append(np.array([[1,3,1,2,3],[11,8,10,8,9]]))
classes.append(np.array([[6,6,7,8,8],[8,10,12,7,8]]))
 


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

def classifier(_classes,x,limit):
	lst = [	]
	index = 0
	for i in _classes:
		temp = {"avg":eculedianDistance( x,average(i) ),"class":i,"index":index}
		lst.append( temp)
		index += 1
	lst.sort(key=lambda x: x['avg'], reverse=False)
	print lst,"\n"
	print lst[0]['avg']," : ",limit
	if float(lst[0]['avg']) > float(limit):
		print "the limit was passed"
		return None
	return 1+lst[0]['index']



if __name__ == '__main__':
	colors = ['magenta', 'black', 'blue', 'brown', 'green']
	x = raw_input("Coordenada x: ")
	y = raw_input("Coordenada y: ")
	p = np.array([[int(x)],[int(y)]])
	limit = raw_input("Limite : ")
	#print p
	#for _class in classes:
	#	print eculedianDistance(p,average(_class))
	result = classifier(classes, p,limit)
	print "\n\n result belong to class {}".format(result)
	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	index = 0
	label = []
	title = []
	for _class in classes:
		temp = ax.scatter(_class[0], _class[1], color=colors[index], marker='.')
		label.append(temp)
		title.append("clase"+str(index+1))
		index += 1

	ax.scatter( x, y, color='red', marker='^')
	ax.legend((label),(title),scatterpoints=1,
        loc='lower left',
        ncol=3,
      	fontsize=8)
	#ax.plot(a, b, color='lightblue', linewidth=3)
	#ax.set_xlim(0, 15)
	#ax.set_ylim(0, 15)
	
	plt.show()
