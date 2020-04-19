# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 12:11:51 2018

@author: Matthew
Project Euler Problem 7 10001st prime
"""
import numpy as np


primes = np.array([2])
testNum = np.array([3])

while primes.size < 10001:
    #Divide the test number by all prime numbers before it
    remainders = np.mod(testNum, primes)
    #If none of the remainders are 0 then testNum is prime
    if not np.any(remainders == 0):
        primes = np.append(primes, testNum[0])
        
    testNum += 1
    
print("10001st Prime is " + str(primes[10000]))