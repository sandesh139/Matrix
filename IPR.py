# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:51:57 2019

@author: Sandesh
"""

#ctrl+1 to comment/uncomment
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def ipr():
    ratio = 0.6
    d = 1
    n = 200
    M = np.zeros((n,n))
    #M = np.identity(n)
    for i in range(0,n-1):
        M[i, i+1] = d + ratio *sp.random.uniform(-1, 1)
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
    IPRList = [];
    for a in range(0,n):
        powerFourSum =0
        
        for b in range(0,n):
            powerFourSum = powerFourSum + eigenvectors[b,a]**4
        
        iprElement = (1/(sp.math.pi**0.5)) * 1/(powerFourSum)
        
        IPRList.append(iprElement)

    return IPRList
