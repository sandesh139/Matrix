# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:17:28 2019

@author: Sandesh
"""

#Information on files

 - binned.txt file has binned data obtained from 15,000 samples of 200*200 matrix
 - binned1.txt file has binned data obtained from 15,000 samples of 200*200 matrix
 - binned22.txt file has binned data obtained from 15,000 samples of 200*200 matrix
 - bin_merge.txt file has merged binned data from binned, binned1 and binned22. It has
2000 lines, which is obtained by binning size of 0.1 from 0 to 200. It has Sum of 10,000,000. 
The sum is obtained from 50,000 simulation of 200 
eigen vectors.
 - IPR.py file has python code for getting the ipr list.
 - BinMerge.py as code for merging the data.
 - simulation.py has code produces binned.txt
 - simulation1.py has code produces binned1.txt
 - simulation2.py has code produces binned22.txt
 - test.pbs, test1.pbs, test2.pbs are the codes for submitting the simulation codes to CARC
 - plot1.png is a plot partitioning the binned data from 0 to 250. 