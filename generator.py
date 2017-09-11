import numpy as np 
from math import sqrt,pow
import random
import matplotlib.pyplot as plt
from matplotlib import animation
from configparser import ConfigParser
from Clasifier import EculedianDistance
from Clasifier import Mahalanobis
from Clasifier import MaxProbability
from Clasifier import KNN


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

	def setPoint(self,x,y):
		self._x = x
		self._y = y

	def closeFigure(self):
		plt.close(self.fig)

	def addClass(self,_class):
		self.classes.append(_class)

	def getNumClasses(self):
		return len(self.classes)

	def getClass(self,x):
		if x < len(self.classes):
			return self.classes[x]
		return None

	def getSample(self,cl):
		index = []
		while (len(index)<len(self.classes[cl][0])/2):
			tmp = random.randint(0,len(self.classes[cl][0])-1)
			if tmp not in index:
 				index.append(tmp)
 		return index

 	def getElement(self,cl,n):
 		return {'x':self.classes[cl][0][n],'y':self.classes[cl][1][n]}
	
	def getElements(self,x,num=False):
		lst = []
		point = {}
		if num == False:
			for dim in range(0,self.classes[x][0].size/self.classes[x][0].ndim):
				lst.append({'x':self.classes[x][0][dim],'y':self.classes[x][1][dim]})
		elif num == True:
			for dim in self.getSample(x):
				lst.append({'x':self.classes[x][0][dim],'y':self.classes[x][1][dim]})
		return lst
					
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

	""" compara un vector para determinar a que clase pertence"""
	def classifier(self,classifierObject,limit):
		x = np.array([[float(self._x)],[float(self._y)]])
		lst = [	]
		index = 0
		#print len(self.classes)
		if isinstance(classifierObject, KNN):
			return classifierObject.distance( x,self.classes)
		else:
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
				if int(limit) != -1:
					if float(lst[0]['distance']) > float(limit):
						print "the limit was passed"
						return None

		#for cl in lst:
		#	print "clase : {} , mean : {} ".format(cl['index']+1,cl['distance'])
		#print lst[0]['avg']," : ",limit
		
		return 1+lst[0]['index']

	def plot(self,x=None,y=None):
		#figure plot logic
		figplot = plt.figure()
		ax = figplot.add_subplot(111)
		cindex = 0
		index = 0
		label = []
		title = []
		for _class in self.classes:
			temp = ax.scatter(_class[0], _class[1], color=self.colors[cindex], marker='.')
			label.append(temp)
			title.append("clase"+str(index+1))
			index += 1
			cindex += 1			
			if cindex == len(self.colors)-1:
				cindex = 0
		if (x != None and y != None):
			ax.scatter( self._x, self._y, color='red', marker='^')
		ax.legend((label),(title),scatterpoints=1,
	        loc='best',
	        ncol=3,
	      	fontsize=8)
		#ax.plot(a, b, color='lightblue', linewidth=3)
		#ax.set_xlim(0, 15)
		#ax.set_ylim(0, 15)
		#a = animation.FuncAnimation(self.fig, self.update, interval=2000,frames=100)
		figplot.show()

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

class Validator(object):
	"""docstring for Validator"""
	def __init__(self, holder, index):
		super(Validator, self).__init__()
		self.holder = holder
		self.classifiers =  [EculedianDistance(),Mahalanobis(),MaxProbability(),KNN()]
		self.index = index

	def sample(self,index,type=False,cl=None):
		if type != None:
			return self.holder.getElements(index,type)
		else:
			return self.holder.getElement(index,cl)


	def check(self,index,type=False,limit=-1):
		#print 
		votes = {}
		for i in range(1,self.holder.getNumClasses()+1):
			votes[i] = 0
		if type != None:
			for x in self.sample(index,type):
				self.holder.setPoint(x['x'],x['y'])
				result = self.holder.classifier(self.classifiers[self.index],limit)
				if result != None:
					votes[result] += 1
			return votes
		else:
			pass
			"""  
				iterate over all class to count votes
				implement getNumElements(Class) in order to use it in a for loop
				use the same structure that if clause
			"""