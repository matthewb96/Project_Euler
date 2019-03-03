# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:04:36 2018
@author: Matthew

Project Euler Problem 3 Largest Prime Factor
Works but extremely slow.
"""

import time
import numpy as np

start = time.clock()
find = 600851475143
primes = np.array([2])
testNum = np.array([3])
factors = np.array([2])

while testNum[0] < (find/2):
    #Divide the test number by all prime numbers before it
    remainders = np.mod(testNum, primes)
    #If none of the remainders are 0 then testNum is prime
    if not np.any(remainders == 0):
        primes = np.append(primes, testNum[0])
        #Check if this prime is a factor
        if np.mod(find , primes[-1]) == 0:
            factors = np.append(factors, primes[-1])
    testNum += 1
    if testNum % 10000 == 0:
        print("Test number: " + str(testNum))

print("Largest prime factor of " + str(find) + " is " + str(factors[-1]))
print("Time taken: " + str(time.clock() - start))