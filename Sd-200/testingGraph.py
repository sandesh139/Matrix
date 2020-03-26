# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 18:49:06 2019

@author: timil
"""

import numpy as np
import matplotlib.pyplot as plt
old = np.loadtxt("old_merge.txt", comments="#", delimiter=",", unpack=False)
new= np.loadtxt("bin_merge.txt", comments="#", delimiter=",", unpack=False)  
plt.plot(old[0:250] , label = 'old')
plt.plot(new[0:250], label = 'new')
plt.legend()