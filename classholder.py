import numpy as np 
from math import sqrt,pow
import random
from Clasifier import EuclideanDistance
from Clasifier import KNN
from Clasifier import Mahalanobis
from Clasifier import MaxProbability

class ClassHolder():
	"""docstring for ClassHolder"""
	def __init__(self, classes=[]):
		self.classes = classes
		self._x = 0
		self._y = 0

	def setPoint(self,x,y):
		self._x = x
		self._y = y

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

 	def getNumElementsByClass(self,cl):
 		return  len(self.classes[cl][0])
	
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

	def classifier(self,classifierObject,points,limit):
		x = np.array(points)
		#print x
		lst = [	]
		index = 0
		#print len(self.classes)
		if isinstance(classifierObject, KNN):
			return classifierObject.distance( x,self.classes)
		else:
			for i in self.classes:
				temp = {"distance":classifierObject.distance( x,i ),"class":i,"index":index}
				#print temp
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
				#print lst
			else:
				lst.sort(key=lambda x: x['distance'], reverse=False	)
				if int(limit) != -1:
					if float(lst[0]['distance']) > float(limit):
						print "the limit was passed"
						return None

		#for cl in lst:
		#	print "clase : {} , mean : {} ".format(cl['index']+1,cl['distance'])
		#print lst[0]['avg']," : ",limit
		
		return lst[0]['index']+1

	def classify(self,classifierObject,points,limit):
		result = self.classifier(classifierObject,points,limit)
		if result != None:
			print "pertenece a la clase : {} ".format(result)
		return result
