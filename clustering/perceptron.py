#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import numpy as np
import matplotlib.pyplot as plt

class Perceptron(object):
    """docstring for Perceptron."""
    def __init__(self,data,r=1):
        self.r = r
        self.w = np.ones(3)
        self.data = data

    def show(self):
        print self.data

    def __minFit(self,i):
        return np.subtract(self.w, self.data[i]*((self.r)) )

    def __maxFit(self,i):
        return np.add(self.w, self.data[i]*((self.r)) )

    def __processData(self):
        change = False
        for i in range(0,len(self.data)):
            if i == 0:
                fsal = np.dot(self.data[i], self.w)
                print fsal
                if fsal >= 0:
                    print "cambio"
                    change = True
                    self.w =self.__minFit(i)
                    print self.w
            else:
                fsal = np.dot(self.data[i], self.w)
                print fsal
                if fsal <= 0:
                    print " clase 2 cambio"
                    change = True
                    self.w =self.__maxFit(i)
                    print self.w
        print "##### fin de iteracion  ######"
        return change

    def process(self):
        end = True
        while(end):
            if not self.__processData():
                end = False
        return self.w

# Función lineal.
def fl(x):
    return 1/2-x

if __name__ == '__main__':
    data  = []
    data.append(np.array([0,0,1]))
    data.append(np.array([0,1,1]))
    data.append(np.array([1,0,1]))
    data.append(np.array([1,1,1]))
    p = Perceptron(data)
    p.show()
    result = p.process()
    print result
    x = [0,0,1,1,2]
    y = [0,1,0,1,2]
    plt.plot(x,y, 'ro')
    x = [x for x in range(-1,1)]
    plt.plot(x, [fl(i) for i in x])
    plt.axis([-2, 2.5, -2, 3.5])
    plt.show()

