# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:31:25 2018
@author: Matthew

Project Euler Problem 1 Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import numpy as np


multiples = np.array([0])

n = 1

while n < 1000:
    #Check if multiple of 3 or 5 and add to array
    if n % 3 == 0 or n % 5 == 0 :
        multiples = np.append(multiples, n)    
    #Add 1 to n 
    n += 1

answer = multiples.sum()
print("Total is: " + str(answer))