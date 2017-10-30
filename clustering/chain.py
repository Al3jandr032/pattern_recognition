#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
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

    def getPointAt(self,index):
        return self.points[index]
    def getMean(self):
        pass
    def addPoint(self, point):
        self.points.append(point)
        self.getMean


g = []
with open('test_data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        aux = Group(row)
        g.append(aux)


print euclidean.distance(g[0].getPointAt(0),g[1].getPointAt(0))
