# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:56:25 2018
@author: Matthew

Project Euler Problem 2 Even Fibonacci numbers
"""

import numpy as np

#Initiate arrays
previousNums = np.array([1, 2])
evenNums = np.array([2])

#Loop through fibonacci sequence
while previousNums[1] <= 4e6:
    newNum = previousNums.sum()
    if newNum % 2 == 0:
        evenNums = np.append(evenNums, newNum)
    #Recreate previous nums array
    previousNums = np.array([previousNums[1], newNum])
    
#Total even nums
total = evenNums.sum()
print("Total even numbers is: " + str(total))