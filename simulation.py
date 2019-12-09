# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:25:46 2019

@author: Sandesh
"""
import numpy as np
import matplotlib.pyplot as plt
from SD import sd
from IPR import ipr
allSDList =[]
allIPR =[]
for i in range(0,1000):
    #allSDList.extend(sd())
    allIPR.extend(ipr())

print("this is size of list ", len(allIPR))
np.savetxt('iprlist.txt', allIPR, delimiter =',')
#np.savetxt('sdlist.txt',allSDList, delimiter= ',')
#plt.hist(allSDList)


