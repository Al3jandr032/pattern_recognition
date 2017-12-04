#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import numpy as np
#import pandas as pd
from perceptron import Perceptron
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    data  = []
    data.append(np.array([0,0,0,1]))
    data.append(np.array([1,0,0,1]))
    data.append(np.array([1,1,0,1]))
    data.append(np.array([1,0,1,1]))

    data.append(np.array([0,0,1,1]))
    data.append(np.array([0,1,1,1]))
    data.append(np.array([0,1,0,1]))
    data.append(np.array([1,1,1,1]))
    p = Perceptron(data,pivot=4,d=4)
    p.show()
    w = p.process()
    w = np.divide(w,np.absolute(w[0]))
    print "resultado : {}".format(w)
    print "Z={}X+{}Y+{}".format(-1*w[0],-1*w[1],-1*w[3])

    # Plot logic
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([0,1,1,1], [0,0,1,0], [0,0,0,1], c='r', marker='^')
    ax.scatter([0,0,0,1], [0,1,1,1], [1,1,0,1], c='b', marker='o')
    xx, yy = np.meshgrid(range(2), range(2))
    z = (-1*w[0] * xx + (-1*w[1]) * yy +(-1*w[3]))
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.plot_surface(xx, yy, z)

    plt.show()
