import numpy as np
binnedData = np.loadtxt("binned.txt", comments="#", delimiter=",", unpack=False)
sumBin = sum(binnedData)

