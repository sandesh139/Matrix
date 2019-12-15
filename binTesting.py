# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:15:08 2019

@author: Sandesh
"""
import numpy as np
from operator import add
import matplotlib.pyplot as plt
binnedData = np.loadtxt("binned.txt", comments="#", delimiter=",", unpack=False)
binnedData1 = np.loadtxt("binned1.txt", comments="#", delimiter=",", unpack=False)
binnedData22 = np.loadtxt("binned22.txt", comments="#", delimiter=",", unpack=False)
mergeData = list(map(add,binnedData,binnedData1))
mergeData = list(map(add,mergeData,binnedData22))
np.savetxt('merge.txt', mergeData, delimiter=',',fmt='%1.0f')
out = np.divide(mergeData, 10000000)                  
sumBin = sum(mergeData)
partitioned = out[0:250]
plt.plot(partitioned)
plt.savefig('plot1.png')