#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import sys
import csv
import numpy as np
from utils import average
from utils import EuclideanDistance

euclidean = EuclideanDistance()
class Group(object):
    def __init__(self, points):
        self.points =  []
        for i in range(0,len(points)):
            points[i] = int(points[i])
        self.points.append(np.array(points))
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

    def compare(self,compare):
        repetidos = 0
        for elem in compare:
            for point in self.points:
                if (elem==point).all():
                    repetidos += 1
                    return True
        """
        if repetidos == len(compare):
            return True
        else:
            return False
        """
def processData(g):
    for i in range(0,len(g)-1):
        dist = euclidean.distance(g[i].getMean(),g[i+1].getMean())
        print dist
        print i," ",g[i].getDelete()
        if dist <= k and not g[i].getDelete():
            if g[i].compare(g[i+1].getPoints()):
                print "force"
                g[i+1].setDelete(force=True)
            else:
                g[i+1].setDelete()
            #print "antes i points ",g[i].getPoints()," : ",g[i+1].getPoints()
            g[i].addPoints(g[i+1].getPoints())
            #print "i points ",g[i].getPoints()
    for elem in g:
        print elem.getDelete()
    return [x for x in g if not x.getDelete()]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        k = float(sys.argv[1])
        g = []
        with open('test_data.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                aux = Group(row)
                g.append(aux)
        kpg = True

        while(kpg):
            origin_size = len(g)
            print "$$$$$$$$$$$$$$$$$$$$$$$$$$$4"
            g = processData(g)
            if len(g) == origin_size:
                kpg = False
            for group in g:
                print group.getPoints()
    else:
        print "introduce el valor de k : {} k".format(sys.argv[0])

"""
print "getPointAt",g[0].getPointAt(0)
print "mean before",g[0].getMean()
g[0].addPoint([3,8])
print "mean after",g[0].getMean()
#print euclidean.distance(g[0].getPointAt(0),g[1].getPointAt(0))
"""
