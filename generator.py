import numpy as np 
from math import sqrt,pow
import matplotlib.pyplot as plt
from matplotlib import animation
from configparser import ConfigParser
from Clasifier import MaxProbability


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
	def __init__(self, classes=[], plotfig=plt.figure()):
		self.classes = classes
		self.fig = plotfig
		self.ax = self.fig.add_subplot(111)
		self.colors = ['b', 'g', 'c', 'm', 'y','k']
		self._x = 0
		self._y = 0
		

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

	def classifier(self,classifierObject,limit):
		x = np.array([[float(self._x)],[float(self._y)]])
		lst = [	]
		index = 0
		print len(self.classes)
		for i in self.classes:
			temp = {"distance":classifierObject.distance( x,i ),"class":i,"index":index}
			lst.append( temp)
			index += 1
		if isinstance(classifierObject, MaxProbability):
			total = 0.0
			for i in lst:
				total += i['distance']
			#print total
			
			for i in lst:
				i['distance'] = (i['distance']/total)*100
			lst.sort(key=lambda x: x['distance'], reverse=True	)
		else:
			lst.sort(key=lambda x: x['distance'], reverse=False	)
			if float(lst[0]['distance']) > float(limit):
				print "the limit was passed"
				return None
		for cl in lst:
			print "clase : {} , mean : {} ".format(cl['index']+1,cl['distance'])
		#print lst[0]['avg']," : ",limit
		
		return 1+lst[0]['index']
		"""
	def update(self,i):
		print "updating {} , {}".format(self._x,self._y)
		cindex = 0
		index = 0
		label = []
		title = []
		for _class in self.classes:
			temp = self.ax.scatter(_class[0], _class[1], color=self.colors[cindex], marker='.')
			label.append(temp)
			title.append("clase"+str(index+1))
			index += 1
			cindex += 1			
			if cindex == len(self.colors)-1:
				cindex = 0
		self.ax.scatter( self._x, int(self._y)+i, color='red', marker='^')
		self.ax.legend((label),(title),scatterpoints=1,
	        loc='best',
	        ncol=3,
	      	fontsize=8)
		plt.clf()
		plt.cla()
		plt.pause(0.05)

	def movePoint(self,x,y):
		self._x = x
		self._y = y
		cindex = 0
		index = 0
		label = []
		title = []
		for _class in self.classes:
			temp = self.ax.scatter(_class[0], _class[1], color=self.colors[cindex], marker='.')
			label.append(temp)
			title.append("clase"+str(index+1))
			index += 1
			cindex += 1			
			if cindex == len(self.colors)-1:
				cindex = 0
		self.ax.scatter( self._x, self._y, color='red', marker='^')
		self.ax.legend((label),(title),scatterpoints=1,
	        loc='best',
	        ncol=3,
	      	fontsize=8)
		a = animation.FuncAnimation(self.fig, self.update, interval=2000,frames=100)
		plt.ion()
		plt.pause(0.05)
	"""
	def classify(self,classifierObject,x,y,limit):
		self._x = x
		self._y = y
		result = self.classifier(classifierObject,limit)
		if result != None:
			print "pertenece a la clase : {} ".format(result)
		#figure plot logic
		cindex = 0
		index = 0
		label = []
		title = []
		for _class in self.classes:
			temp = self.ax.scatter(_class[0], _class[1], color=self.colors[cindex], marker='.')
			label.append(temp)
			title.append("clase"+str(index+1))
			index += 1
			cindex += 1			
			if cindex == len(self.colors)-1:
				cindex = 0
		self.ax.scatter( self._x, self._y, color='red', marker='^')
		self.ax.legend((label),(title),scatterpoints=1,
	        loc='best',
	        ncol=3,
	      	fontsize=8)
		#ax.plot(a, b, color='lightblue', linewidth=3)
		#ax.set_xlim(0, 15)
		#ax.set_ylim(0, 15)
		#a = animation.FuncAnimation(self.fig, self.update, interval=2000,frames=100)
		return self.ax
		#return{'belongClass':result,'label':label,'title':title}
	

		