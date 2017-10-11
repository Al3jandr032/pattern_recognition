import numpy as np 
from math import sqrt,pow
import matplotlib.pyplot as plt

classes = []
classes.append(np.array([[1,3,1,2,3],[2,5,5,2,3],[2,5,5,2,3]]))
classes.append(np.array([[6,6,7,8,8],[4,3,4,4,5],[2,5,5,2,3]]))
classes.append(np.array([[10,12,10,15,10],[11,11,13,14,12],[2,5,5,2,3]]))
classes.append(np.array([[1,3,1,2,3],[11,8,10,8,9],[2,5,5,2,3]]))
classes.append(np.array([[6,6,7,8,8],[8,10,12,7,8],[2,5,5,2,3]]))
 
def average(numArray):
	res = np.zeros( (numArray.shape[0],1) )
	index = 0
	for dim in numArray:
		avg = 0.0
		for element in dim:
			avg += element
		avg = avg/dim.size
		res[index] = avg
		index += 1
	return res

def EuclideanDistance(avg1,avg2):
	tmp = 0.0
	if avg1.shape[0] == avg2.shape[0]:
		for x in range(0,avg2.shape[0]):
			tmp += pow(avg1[x]-avg2[x],2)
	return sqrt(tmp)

def classifier(_classes,x,limit):
	lst = [	]
	index = 0
	for i in _classes:
		temp = {"avg":EuclideanDistance( x,average(i) ),"class":i,"index":index}
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
	x = 1
	y = 1
	z = 1
	p = np.array([[int(x)],[int(y)],[int(z)]])
	limit = 20
	#print p
	#for _class in classes:
	#	print eculedianDistance(p,average(_class))
	result = classifier(classes, p,limit)
	print "\n\n result belong to class {}".format(result)
	"""
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
	"""