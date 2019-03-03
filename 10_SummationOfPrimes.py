# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 15:53:21 2018

@author: Matthew
Project Euler Problem 10 Summation of primes
"""
import numpy as np

upper = 2000000
primes = np.arange(2, upper + 1)

for i in primes:
    pos,  = np.where(primes == i)
    remainders = np.mod(primes, i)
    indices, = np.where(remainders == 0)
    primes = np.delete(primes, indices[1:])
    
    if i**2 > upper:
        primes = primes.astype(float) #Need to change dtype because sum is too large for int dtype
        print("The sum of primes below {} is {}".format(str(upper), str(primes.sum())))
        break
