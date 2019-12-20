# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:33:31 2019

@author: Sandesh
"""

import numpy as np
import random
import matplotlib.pyplot as plt




def sd():
    ratio = 0.6
    d = 1
    n = 200
    M = np.zeros((n,n))
    #M = np.identity(n)
    for i in range(0,n-1):
        M[i, i+1] = d + ratio *random.uniform(-1, 1)
        M[i+1,i] = M[i,i+1]
    #print ("this is M\n\n", M)
    eigenvalues, eigenvectors = np.linalg.eig(M)
    #eigen vectors are already normalized
    
    
    listMean =[]
    for q in range(0,n):
        mean = 0
        for p in range(0,n):
            mean = mean + (p+1) *(eigenvectors[p][q]**2)
        listMean.append(mean)
    SDList = [];
   
    for a in range(0,n):
        variance = 0
        for b in range(0,n):
            variance = variance + ((b+1-listMean[a])**2) * (eigenvectors[b,a]**2) 
        rootvariance = variance**0.5
        SDList.append(rootvariance)

    return SDList
