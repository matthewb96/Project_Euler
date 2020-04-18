# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:04:53 2018

@author: Matthew
Project Euler Problem 12 Highly divisible triangular number
"""

import sys
import numpy as np
  
numFactors = 500 #Number of factors needed

#Loop through triangle numbers until found a number with the number of factors wanted
num = 2
while True:
    newTrian = np.sum(np.arange(num, dtype = int))
    factors = 0
    for i in range(1, int(np.rint(np.sqrt(newTrian))) + 1):
        if newTrian / i == i:
            factors += 1
        elif newTrian % i == 0:
            factors += 2
        if factors >= numFactors:
            print(str(newTrian) + " has " + str(factors))
            sys.exit()
    num += 1
    if factors % 10 == 0:
        print("Factors found " + str(factors) + " for " + str(newTrian))
