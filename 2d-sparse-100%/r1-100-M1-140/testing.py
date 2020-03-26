# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:13:24 2020

@author: timil
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()




import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import sparse
import scipy as sp
def SdIpr():
    ratio = 1
    M1 = 140
    N1 = M1**2
#    M = np.zeros((N1,N1))
    d0 =1
    rowList=[]
    colList=[]
    dataList = []
    for i in range (0,N1):
        if(i%M1 != (M1-1)):
#            M[i,i+1] = d0 + ratio *random.uniform(-1, 1)
            rowList.append(i)
            colList.append(i+1)
            dataList.append(d0 + ratio *random.uniform(-1, 1))
        if(i%M1 != 0):
#            M[i,i-1] = d0 + ratio *random.uniform(-1, 1)
            rowList.append(i)
            colList.append(i-1)
            dataList.append(d0 + ratio *random.uniform(-1, 1))
        if(i+M1 < N1):
#            M[i,i+M1] =  d0 + ratio *random.uniform(-1, 1)
            rowList.append(i)
            colList.append(i+M1)
            dataList.append(d0 + ratio *random.uniform(-1, 1))
        if(i-M1>= 0):
#            M[i,i-M1] =  d0 + ratio *random.uniform(-1, 1)
            rowList.append(i)
            colList.append(i-M1)
            dataList.append(d0 + ratio *random.uniform(-1, 1))
    
    
        
    sparseM = sparse.csr_matrix((np.array(dataList), (np.array(rowList), np.array(colList))))
   

    
    
    
    symM = (sparseM + sparse.csr_matrix.transpose(sparseM)) *0.5
    matrix = symM.todense()
    symM = 0
    sparseM =0
 
  
    
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    matrix = 0
    

    listSDV = []
    listIPR = []
    for z in range (0,N1):
        eigenVecMatrix = eigenvectors[:,z].reshape(M1,M1)
        meanj = 0
        meank = 0
        for p in range(0,M1):
            for q in range(0,M1):
                
                meanj = meanj + (p+1)*(eigenVecMatrix[p,q]**2)
                meank = meank + (q+1)*(eigenVecMatrix[p,q]**2)
            
        variance =0
        iprSum =0
        for s in range(0,M1):
            for t in range(0,M1):
                variance = variance + ((s+1-meanj)**2 + (t+1-meank)**2)* \
                (eigenVecMatrix[s,t]**2)
                iprSum = iprSum + eigenVecMatrix[s,t] **4
               
   
        rootIpr = ((1/sp.math.pi) *(1/iprSum))**0.5
        rootVariance = (2**0.5) *(variance **0.5)
        listSDV.append(rootVariance)
        listIPR.append(rootIpr)
        
    return listSDV,listIPR

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros
if (rank%4 == 0 ):
    Partition = np.linspace(0,140,1400)    
    dataIPR = zerolistmaker(len(Partition)) 
    dataSD = zerolistmaker(len(Partition))    
    for i in range(0,13):
        allSD, allIPR = SdIpr()
        sortedList = np.searchsorted(Partition,allIPR)
        frequency = np.bincount(sortedList)[1:]
        for i in range(0,len(frequency)):
            dataIPR[i] = dataIPR[i] + frequency[i]
            sortedListSD = np.searchsorted(Partition,allSD)
            frequencySD = np.bincount(sortedListSD)[1:]
            
        for i in range(0,len(frequencySD)):
            dataSD[i] = dataSD[i] + frequencySD[i]         


       
    np.savetxt('binnedIPR'+str(rank)+'.dat', dataIPR, delimiter=',',fmt='%1.0f') 
    np.savetxt('binnedSD'+str(rank)+'.dat', dataSD, delimiter=',',fmt='%1.0f') 

    