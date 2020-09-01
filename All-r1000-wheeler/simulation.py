# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:25:46 2019

@author: Sandesh
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import scipy as sp
import math



from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()



#from SD import sd
def SdIpr(testSize):
    ratio = 10
    d = 1
    n = testSize
    M = np.zeros((n,n))
    #M = np.identity(n)
    for i in range(0,n-1):
        M[i, i+1] = d
        M[i+1,i] = d
        M[i,i] = ratio *random.uniform(-1, 1)
    M[n-1,n-1] = ratio *random.uniform(-1, 1)
   
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
        rootvariance =2* variance**0.5
        SDList.append(rootvariance)
        
        
    IPRList = [];
    for a in range(0,n):
        powerFourSum =0
        
        for b in range(0,n):
            powerFourSum = powerFourSum + eigenvectors[b,a]**4
        
        iprElement = (1/(sp.math.pi**0.5)) * 1/(powerFourSum)
        
        IPRList.append(iprElement)    
    return SDList,IPRList


def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros


for mSize in range(1,41):
    test = 10 *mSize
    Partition = np.linspace(0,test,test*10)    
    dataIPR = zerolistmaker(len(Partition)) 
    dataSD = zerolistmaker(len(Partition))
    iterTimes = math.ceil(50000000/(128*test))
    print("test size " +str(test));
    for i in range(0,iterTimes):
        allSD, allIPR = SdIpr(test)
        sortedList = np.searchsorted(Partition,allIPR)
        frequency = np.bincount(sortedList)[1:]
    
        for i in range(0,len(frequency)):
            dataIPR[i] = dataIPR[i] + frequency[i]    

        sortedListSD = np.searchsorted(Partition,allSD)
        frequencySD = np.bincount(sortedListSD)[1:]
        for i in range(0,len(frequencySD)):
            dataSD[i] = dataSD[i] + frequencySD[i] 
        
        
        
    np.savetxt(str(test)+'binnedIPR'+str(rank)+'.dat', dataIPR, delimiter=',',fmt='%1.0f') 
    np.savetxt(str(test) +'binnedSD'+str(rank)+'.dat', dataSD, delimiter=',',fmt='%1.0f') 
    print("this is sum of dataSD ", sum(dataSD))
    print("this is sum of dataIPR ", sum(dataIPR))






