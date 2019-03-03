# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:50:54 2018

@author: Matthew
Project Euler Problem 14 Longest Collatz sequence
"""

import numpy as np


def genSequence(start):
    """
    Generates Collatz sequence starting with start.
    """
    sequence = np.array([start], dtype = int)
    while sequence[-1] != 1:
        num = sequence[-1]
        if num % 2 == 0: #If even
            value = num/2
        else: #If odd
            value = (3 * num) + 1
        #Add to sequence
        sequence = np.append(sequence, value)
    return sequence


#Test values up to 1million
longestLength = 0
for i in range(1, 1000000):
    sequence = genSequence(i)
    if len(sequence) > longestLength:
        longestLength = len(sequence)
        longestStart = sequence[0]
        print("Longest sequence so far is " + str(longestLength) + " with start of " + str(longestStart))
        
print("Longest sequence overall is " + str(longestLength) + " with start of " + str(longestStart))