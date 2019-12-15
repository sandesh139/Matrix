# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:25:46 2019

@author: Sandesh
"""
import numpy as np
import matplotlib.pyplot as plt
#from SD import sd
from IPR import ipr
allSDList =[]
allIPR =[]

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros
#for i in range(0,1000):
#    #allSDList.extend(sd())
#    allIPR =ipr()
#    f = open('iprList.txt','a')
#    np.savetxt(f, allIPR ,fmt='%1.3f',delimiter =',')
#    f.close()
Partition = np.linspace(0,200,2000)    
datas = zerolistmaker(len(Partition))   
for i in range(0,200):
    allIPR = ipr()
    sortedList = np.searchsorted(Partition,allIPR)
    frequency = np.bincount(sortedList)[1:]
    for i in range(0,len(frequency)):
        datas[i] = datas[i] + frequency[i]        
np.savetxt('binned.txt', datas, delimiter=',',fmt='%1.0f')    
print("this is size of list ", len(allIPR))
#np.savetxt('iprlist.txt', allIPR, delimiter =',')
#np.savetxt('sdlist.txt',allSDList, delimiter= ',')
#plt.hist(allSDList)


