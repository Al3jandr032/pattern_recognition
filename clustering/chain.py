#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import sys
import csv
import numpy as np
from PIL import Image
from utils import average
from utils import EuclideanDistance

euclidean = EuclideanDistance()
class Group(object):
    def __init__(self, point=[]):
        
        self.points =  []
        #for i in range(0,len(point)):
        #    point[i] = int(point[i])
        self.points.append(np.array(point))
        self.mean = self.points[0]
        self.delete = False
        self.force = False


    def getPointAt(self,index):
        return self.points[index]

    def getPoints(self):
        return self.points

    def Mean(self):
        return self.mean

    def setDelete(self,force=False):
        self.delete = True
        self.force = force

    def getDelete(self):
        if self.force:
            return True
        elif len(self.points)>1:
            return False
        else:
            return self.delete

    def getMean(self):
        if len(self.points)==1:
            return self.points[0]
        else:
            mean = np.zeros(2)
            for i in self.points:
                mean[0] += i[0]
                mean[1] += i[1]
            mean[0] = mean[0]/len(self.points)
            mean[1] = mean[1]/len(self.points)
            return mean

    def addPoint(self, point):
        self.points.append(np.array(point))
        self.mean = self.getMean()

    def addPoints(self,points):
        for p in points:
            if not any((p == x).all() for x in self.points):
                self.points.append(p)
        self.mean = self.getMean()

def processData(umbral,g):
    print "Numero de clases :  ",(len(g)-1)
    for i in range(0,len(g)-1):
        dist = euclidean.distance(g[i].getMean(),g[i+1].getMean())
        #print dist
        #print i," ",g[i].getDelete()
        if dist <= umbral and not g[i].getDelete():
            #print "\n\n\t",dist
            if np.array_equal(g[i].getPoints,g[i+1].getPoints()):
                g[i+1].setDelete(force=True)
            elif i==len(g)-2:
                g[i+1].setDelete(force=True)
            else:
                g[i+1].setDelete()
            g[i].addPoints(g[i+1].getPoints())
            #print dist
    
    return [x for x in g if not x.getDelete()]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        g = []
        k = int(sys.argv[2])
        im = Image.open(sys.argv[1])
        pix = im.load()
        
        for i in range(0,im.size[0],50):
            for j in range(0,im.size[1],50):
                aux = Group(pix[i,j])
                #print aux.getPoints()
                g.append(aux)
        
        """
        with open('test_data.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                aux = Group(row)
                g.append(aux)
        """
        
        
        for umbral in range(k-1,k):
            aux = g
            kpg = True
            print "validando umbral con : {}".format(umbral)
            while(kpg):
                origin_size = len(aux)
                print "######## Starting process ##################"
                #print origin_size
                aux = processData(umbral,aux)
                if len(aux) == origin_size:
                    kpg = False
                print len(aux)
                if len(aux) < 5:
                    break
            print "numero de clases : ",len(aux)-2
            """
            for group in g:
                print group.getPoints()
            """
    else:
        print "use : {} k <file-path>".format(sys.argv[0])

"""
print "getPointAt",g[0].getPointAt(0)
print "mean before",g[0].getMean()
g[0].addPoint([3,8])
print "mean after",g[0].getMean()
#print euclidean.distance(g[0].getPointAt(0),g[1].getPointAt(0))
"""
