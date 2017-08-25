import numpy as np 
from math import sqrt,pow
import matplotlib.pyplot as plt
from configparser import ConfigParser


def eculedianDistance(avg1,avg2):
		return sqrt(pow(avg1[0]-avg2[0],2)+pow(avg1[1]-avg2[1],2))

class ClassGenerator(object):
	"""docstring for ClassGenerator"""
	def __init__(self, n=0,size=0,config_path=None):
		super(ClassGenerator, self).__init__()
		self.n = int(n)
		self.size = int(size)
		self.path = config_path
		
	def generate(self):
		lst = []
		if self.path != None:
			parser = ConfigParser()
			parser.read(self.path)
			for section_name in parser.sections():
				d = parser.get(section_name, 'd')
				x = parser.get(section_name, 'x')
				y = parser.get(section_name, 'y')
				tmp =  np.random.randn(2, self.size)
				tmp[0] = float(d)*tmp[0]+float(x)
				tmp[1] = float(d)*tmp[1]+float(y)
				lst.append(tmp)
		else:
			for i in xrange(0,self.n):
				d = raw_input("introduce la dispercion de la clase "+str(i)+" :")
				x = raw_input("introduce la posicion en x de la clase "+str(i)+" :")
				y = raw_input("introduce la posicion en y de la clase "+str(i)+" :")
				tmp =  np.random.randn(2, self.size)
				tmp[0] = float(d)*tmp[0]+float(x)
				tmp[1] = float(d)*tmp[1]+float(y)
				lst.append(tmp)
		return lst



class ClassHolder(object):
	"""docstring for ClassHolder"""
	def __init__(self, classes=[]):
		super(ClassHolder, self).__init__()
		self.classes = classes

	def addClass(self,_class):
		self.classes.append(_class)
	
	def average(self,numArray):
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

	

	def classifier(self,type,x,limit):
		lst = [	]
		index = 0
		for i in self.classes:
			temp = {"avg":type( x,self.average(i) ),"class":i,"index":index}
			lst.append( temp)
			index += 1
		lst.sort(key=lambda x: x['avg'], reverse=False)
		for cl in lst:
			print "clase : {} , mean : {} ".format(cl['index']+1,cl['avg'])
		#print lst[0]['avg']," : ",limit
		if float(lst[0]['avg']) > float(limit):
			print "the limit was passed"
			return None
		return 1+lst[0]['index']

	def classify(self,type):
		colors = ['b', 'g', 'c', 'm', 'y','k']
		x = raw_input("Coordenada x: ")
		y = raw_input("Coordenada y: ")
		p = np.array([[float(x)],[float(y)]])
		limit = raw_input("Limite : ")
		
		result = self.classifier(type,p,limit)
		print "\n\n Result belong to class {}".format(result)
		#figure plot logic
		fig = plt.figure()
		ax = fig.add_subplot(111)
		cindex = 0
		index = 0
		label = []
		title = []
		for _class in self.classes:
			temp = ax.scatter(_class[0], _class[1], color=colors[cindex], marker='.')
			label.append(temp)
			title.append("clase"+str(index+1))
			index += 1
			cindex += 1			
			if cindex == len(colors)-1:
				cindex = 0
		
		ax.scatter( x, y, color='red', marker='^')
		ax.legend((label),(title),scatterpoints=1,
	        loc='best',
	        ncol=3,
	      	fontsize=8)
		#ax.plot(a, b, color='lightblue', linewidth=3)
		#ax.set_xlim(0, 15)
		#ax.set_ylim(0, 15)
		
		plt.show()
